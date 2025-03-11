import pathlib
import typing

from .pip import required

if typing.TYPE_CHECKING:
    from tqdm import tqdm


def download(url, dst, *requests_args, unlink_if_exists=True, chunk_size=1024 * 1024, show_progress=False, **requests_kwargs):
    required('requests')
    import requests

    dst = pathlib.Path(dst)

    if dst.exists():
        if unlink_if_exists:
            dst.unlink()
        else:
            raise FileExistsError(dst)

    if show_progress:
        required('tqdm')
        from tqdm import tqdm
    else:
        tqdm = None

    tmp_file = pathlib.Path(dst.parent / (dst.name + '.tmp'))
    _i = 0
    while tmp_file.exists():
        _i += 1
        tmp_file = pathlib.Path(dst.parent / (dst.name + f'.tmp.{_i}'))

    with requests.get(url, stream=True, *requests_args, **requests_kwargs) as r:
        r.raise_for_status()
        if show_progress:
            total = int(r.headers.get('content-length', 0))
            print(f'Downloading {url}')
            pbar = tqdm(total=total, unit='B', unit_scale=True, unit_divisor=1024)
        else:
            pbar = None

        with tmp_file.open('wb') as f:
            for chunk in r.iter_content(chunk_size):
                f.write(chunk)
                if pbar:
                    pbar.update(len(chunk))

    tmp_file.rename(dst)
    return dst
