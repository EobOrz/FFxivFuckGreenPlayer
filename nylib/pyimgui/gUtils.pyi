from __future__ import annotations
import typing
__all__ = ['PyCtxWrapper']
class PyCtxWrapper:
    def __enter__(self) -> typing.Any:
        ...
    def __exit__(self, *args) -> None:
        ...
