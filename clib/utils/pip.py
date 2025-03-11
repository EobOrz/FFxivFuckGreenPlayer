import logging
import os
import socket
import urllib.request
import urllib.error
import urllib.parse
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning, module=".*packaging\\.version")

PIP_SOURCE = {
    'PYPI': 'https://pypi.python.org/simple',
    # mirror sites in China...
    '阿里云': 'https://mirrors.aliyun.com/pypi/simple/',
    '腾讯云': 'https://mirrors.cloud.tencent.com/pypi/simple/',
    '北外大学': 'https://mirrors.bfsu.edu.cn/pypi/web/simple',
    '清华大学': 'https://pypi.tuna.tsinghua.edu.cn/simple',
    '网易': 'https://mirrors.163.com/pypi/simple/',
}

_logger = logging.getLogger(__name__)


def boostrap_pip():
    """
    If pip is not installed, it uses the `ensurepip` module to bootstrap it.
    """
    try:
        import pip
    except ImportError:
        import ensurepip

        ensurepip.bootstrap()

        import pip


def _test_pip_source(url):
    try:
        return urllib.request.urlopen(url, timeout=5).getcode() == 200
    except (urllib.error.HTTPError, urllib.error.URLError, socket.timeout):
        return False


def _set_pip_default_index(url: str):
    import pip._internal.cli.cmdoptions as cmdoptions

    options: list = cmdoptions.general_group["options"]

    if not hasattr(cmdoptions, '_config_default_index'):
        cmdoptions._original_trust_host_getter = cmdoptions.trusted_host
        cmdoptions._original_trust_host_index = options.index(cmdoptions._original_trust_host_getter)
        cmdoptions._config_default_index = True

    cmdoptions.index_url.keywords['default'] = url

    def new_trust_host_getter():
        res = cmdoptions._original_trust_host_getter()
        res.default.append(urllib.parse.urlparse(url).netloc)
        return res

    options[cmdoptions._original_trust_host_index] = new_trust_host_getter


def set_pip_default_index(manual_url: str = None):
    """
    This function sets the default pip index.
    If `manual_url` is not None, it will use the specified URL.
    Otherwise, it will test the URLs in `PIP_SOURCE` and use the first available URL.
    :param manual_url:
    :return:
    """
    boostrap_pip()

    if manual_url is not None:
        _set_pip_default_index(manual_url)
        set_pip_default_index.is_set = True
        return True

    if hasattr(set_pip_default_index, 'is_set'): return True
    for name, url in PIP_SOURCE.items():
        if _test_pip_source(url):
            _logger.info(f'Usable pip source: {name} {url}')
            _set_pip_default_index(url)
            set_pip_default_index.is_set = True
            return True
    raise Exception('No usable pip source found')


def install(*_a):
    """
    This function installs the specified packages using pip.
    Use arguments same as `pip install`.
    :param _a:
    :return: True if the installation is successful.
    """
    boostrap_pip()

    import pip._internal.commands
    import pip._internal.cli.status_codes

    set_pip_default_index()
    # pip._internal.commands.install.InstallCommand
    try:
        if pip._internal.commands.create_command('install').main(list(_a)) == pip._internal.cli.status_codes.SUCCESS:
            return True
    except SystemExit as e:
        pass

    raise RuntimeError('Failed to install requirements, read the log for more information')


def is_installed(*_a):
    """
    This function checks if the specified packages are installed.
    Use arguments same as `pip show`.
    :param _a:
    :return: True if all packages are installed.
    """
    boostrap_pip()

    import pip._internal.commands.show

    required = len(_a)
    for _ in pip._internal.commands.show.search_packages_info(_a):
        required -= 1
        if required == 0: return True
    return False

if os.environ.get('PYTHON_PIP_ALL_REQ_INSTALLED'):
    required = lambda *_a: True
else:
    def required(*_a):
        """
        This function checks if the specified packages are installed.
        If not, it installs them.
        Use arguments same as `pip install`.
        :param _a:
        :return: True if all packages are installed.
        """
        if not is_installed(*_a):
            return install(*_a)
        return True
