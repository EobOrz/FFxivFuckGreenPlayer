import base64
import pathlib
import pickle
import zlib

finder_identifier = '_IsNyPkgArchiveFinder0001'

template_main = f'''
def __pkg_loader__(archive_code):
    import sys
    for _finder in sys.meta_path:
        if hasattr(_finder, {finder_identifier!r}):
            finder = _finder
            break
    else:
        import base64,importlib.abc,importlib.machinery,importlib.util,inspect,pickle,zlib
        class _NyPkgArchiveLoader(importlib.abc.Loader):
            def __init__(self, code): self.code = code
            def create_module(self, spec): return None
            def exec_module(self, module): exec(self.code, module.__dict__)
        class _NyPkgArchiveFinder(importlib.abc.MetaPathFinder):
            def __init__(self): self.archive = {{}}
            def reg(self, name, archive):
                prefix = '' if name == '__main__' else name + '.'
                for _name, data in pickle.loads(zlib.decompress(base64.b85decode(archive))).items(): self.archive[prefix + _name] = data
            def exec_pkg(self, name, globals_):
                try:
                    f = inspect.currentframe().f_back
                    name = f.f_globals['__name__']
                    while f.f_code.co_name != 'exec_module': f = f.f_back
                    module = f.f_locals['module']
                    assert module.__name__ == name
                except Exception as e:
                    pass
                else:
                    module.submodule_search_locations = []
                    module.__path__ = ''
                if _data := self.archive.get('__main__' if name == '__main__' else name + '.__init__'):
                    exec(_data[0], globals_)
            def find_spec(self, fullname, path, target=None):
                if fullname in self.archive:
                    code, is_pkg = self.archive[fullname]
                    return importlib.util.spec_from_loader(fullname, _NyPkgArchiveLoader(code), is_package=is_pkg)
                return None
        setattr(_NyPkgArchiveFinder, {finder_identifier!r}, True)
        sys.meta_path.append(finder := _NyPkgArchiveFinder())
    finder.reg(__name__, archive_code)
    globals().pop('__pkg_loader__', None)
    finder.exec_pkg(__name__, globals())
'''.strip()

template = f'''
def __pkg_loader__(archive_code):
    import sys
    for finder in sys.meta_path:
        if hasattr(finder, {finder_identifier!r}):
            finder.reg(__name__, archive_code)
            globals().pop('__pkg_loader__', None)
            finder.exec_pkg(__name__, globals())
            return
    raise Exception('finder not found')
'''.strip()


def pack(p: str | pathlib.Path, o=None, is_main: bool = True):
    o = o or (lambda x: x)
    p = p if isinstance(p, pathlib.Path) else pathlib.Path(p)
    assert p.exists(), 'path not exists'
    if p.is_file():
        return o(p.read_bytes())
    data = {}
    for _p in p.iterdir():
        if _p.is_file():
            if _p.suffix == '.py' or _p.suffix == '.pyw':
                data[_p.stem] = o(_p.read_bytes()), False
        elif _p.name != '__pycache__' and (_p / '__init__.py').exists():
            data[_p.stem] = pack(_p, o, False), True
    decoded = base64.b85encode(zlib.compress(pickle.dumps(data))).decode('utf-8')
    return (template_main if is_main else template) + f'\n__pkg_loader__({decoded!r})\n'
