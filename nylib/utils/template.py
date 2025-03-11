import functools
import threading
import typing

A_T = typing.TypeVar('A_T')
R_T = typing.TypeVar('R_T')


class template:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __call__(self, callable_: typing.Callable[..., R_T]) -> '_template[R_T]':
        return _template(self.kwargs, callable_)


class _template(typing.Generic[R_T]):
    def __init__(self, defs, callable_: typing.Callable[..., R_T]):
        self.define = defs
        self.callable = callable_

    def t(self, *args, **kwargs) -> typing.Callable[..., R_T]:
        params = self.define.copy()
        for a, k in zip(args, self.define.keys()): params[k] = a
        params.update(kwargs)
        return self._make(params)

    def __call__(self, *args, **kwargs) -> R_T:
        return self._make(self.define)(*args, **kwargs)

    def _make(self, params):
        @functools.wraps(self.callable)
        def wrapper(*args, **kwargs):
            with _TemplateArg(params):
                return self.callable(*args, **kwargs)

        return wrapper


class _TemplateArg:
    def __init__(self, params):
        self.params = params

    def __enter__(self):
        if not hasattr(template_args.tbl, 'args'):
            template_args.tbl.args = []
        template_args.tbl.args.append(self.params)

    def __exit__(self, exc_type, exc_val, exc_tb):
        args = template_args.tbl.args
        args.pop()
        if not args:
            del template_args.tbl.args


class _TemplateArgs:
    tbl = threading.local()

    def __getattr__(self, item):
        if (args := getattr(self.tbl, 'args', None)) is None:
            raise AttributeError('No template arguments')
        return args[-1][item]


template_args = _TemplateArgs()


def test():
    @template(a=1, t=int)
    def func(n):
        return template_args.t(template_args.a) + n

    print(func(1))
    print(func.t(2, float)(1))


if __name__ == '__main__':
    test()
