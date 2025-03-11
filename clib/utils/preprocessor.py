# $RAISE "Preprocessor is already imported, dont reload it"

# default support macros
# - $SYM_FROM [Name] [Module] [Expr] : define a symbol from a module value
# - $SYM [Name] [Expr] : define a symbol
# - $INCLUDE [Name]: include a file with predefined symbols, absolute name only
# - $IF [Expr] / $ELSE / $ELIF [Expr] / $ENDIF: conditional compilation
# - $RAISE [Message]: throw an exception
# - $REQUIRE [Pip Modules...]: check if the module is available, if not, automatically install it
# - use `__SYM_[Name]` in code to use the symbol


import builtins
import importlib
import re
import sys

old_exec = builtins.exec
old_compile = builtins.compile

_re_is_comment = re.compile(r'^\s*#')
_re_symbol = re.compile(r'__SYM_([a-zA-Z_][a-zA-Z0-9_]*)')


class IProcessors:
    symbols: dict
    enable = False
    _reged = []

    def __init_subclass__(cls, **kwargs):
        cls._reged.append(cls)

    def __init__(self, symbols):
        self.symbols = symbols

    def process_code(self, code):
        return code

    def process_comment(self, comment):
        return comment


class BasicProcessor(IProcessors):
    enable = True

    def __init__(self, *a):
        super().__init__(*a)
        self.cond_stack = []

    def process_code(self, code):
        if self.cond_stack and not self.cond_stack[-1][0]:
            return
        return _re_symbol.sub(lambda m: repr(self.symbols.get(m.group(1), m.group(0))), code)

    def process_comment(self, comment):
        args = comment.strip().split()
        if len(args) == 0: return
        match args[0]:
            case '$IF':
                if len(args) < 2:
                    raise SyntaxError('Invalid $IF statement, expected $IF [Expr]')
                is_true = bool(eval(' '.join(args[1:]), None, self.symbols))
                self.cond_stack.append((is_true, is_true))
                raise StopIteration
            case '$ELSE':
                if not self.cond_stack:
                    raise SyntaxError('Invalid $ELSE statement, no matching $IF')
                _, is_processed = self.cond_stack[-1]
                is_true = not is_processed
                self.cond_stack[-1] = (is_true, is_processed)
                raise StopIteration
            case '$ELIF':
                if len(args) < 2:
                    raise SyntaxError('Invalid $ELIF statement, expected $ELIF [Expr]')
                if not self.cond_stack:
                    raise SyntaxError('Invalid $ELIF statement, no matching $IF')
                _, is_processed = self.cond_stack[-1]
                if is_processed:
                    self.cond_stack[-1] = (False, True)
                    raise StopIteration
                is_true = bool(eval(' '.join(args[1:]), None, self.symbols))
                self.cond_stack[-1] = (is_true, is_true)
                raise StopIteration
            case '$ENDIF':
                if not self.cond_stack:
                    raise SyntaxError('Invalid $ENDIF statement, no matching $IF')
                self.cond_stack.pop()
                raise StopIteration
        if self.cond_stack and not self.cond_stack[-1][0]:
            raise StopIteration
        match args[0]:
            case '$SYM_FROM':
                if len(args) < 4:
                    raise SyntaxError('Invalid $DEFINEFROM statement, expected $DEFINEFROM [Name] [Module] [Expr]')
                self.symbols[args[1]] = eval(' '.join(args[3:]), None, importlib.import_module(args[2]).__dict__)
                raise StopIteration
            case '$SYM':
                if len(args) < 2:
                    raise SyntaxError('Invalid $DEFINE statement, expected $DEFINE [Name] [Expr?]')
                if len(args) > 2:
                    val = eval(' '.join(args[2:]), None, self.symbols)
                else:
                    val = None
                self.symbols[args[1]] = val
                raise StopIteration
            case '$INCLUDE':
                if len(args) < 2:
                    raise SyntaxError('Invalid $INCLUDE statement, expected $INCLUDE [Name]')
                module = importlib.import_module(args[1])
                self.symbols.update(getattr(module, '__preprocess_symbols__', {}))
                raise StopIteration
            case '$RAISE':
                if len(args) < 2:
                    raise SyntaxError('Invalid $RAISE statement, expected $RAISE [Message]')
                raise Exception(' '.join(args[1:]))
            case '$REQUIRE':
                from . import pip
                if len(args) < 2:
                    raise SyntaxError('Invalid $REQUIRE statement, expected $REQUIRE [Pip Modules...]')
                if not pip.is_installed(*args[1:]):
                    pip.install(*args[1:])
                raise StopIteration
        return comment


def preprocess(code):
    codes = []
    prev = ''
    is_code = True
    for line in code.splitlines():
        if m := _re_is_comment.match(line):
            if is_code and prev:
                codes.append((prev, is_code))
                prev = ''
            is_code = False
            if prev: prev += ' '
            prev += line[m.end():].strip()
            if prev.endswith('\\'):
                prev = prev[:-1]
            else:
                codes.append((prev, is_code))
                prev = ''
        else:
            if not is_code and prev:
                codes.append((prev, is_code))
                prev = ''
            is_code = True
            if prev: prev += '\n'
            prev += line

    if prev:
        codes.append((prev, is_code))
    # print(codes)
    symbols = {}
    processors = [c(symbols) for c in IProcessors._reged if c.enable]
    res = ''

    for c, is_code in codes:
        if is_code:
            try:
                for p in processors:
                    if not (c := p.process_code(c)):
                        raise StopIteration
            except StopIteration:
                continue
            res += c + '\n'
        else:
            try:
                for p in processors:
                    if not (c := p.process_comment(c)):
                        raise StopIteration
            except StopIteration:
                continue
            res += '# ' + c + '\n'
    res += '__preprocess_symbols__ = ' + repr(symbols)
    # print(res)
    return res


def new_exec(code, __globals=None, __locals=None):
    if isinstance(code, bytes):
        code = preprocess(code.decode('utf-8'))
    elif isinstance(code, str):
        code = preprocess(code)
    return old_exec(code, __globals, __locals)


def new_compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1):
    if mode == 'exec':
        if isinstance(source, bytes):
            source = preprocess(source.decode('utf-8'))
        elif isinstance(source, str):
            source = preprocess(source)
    return old_compile(source, filename, mode, flags, dont_inherit, optimize)


def new_cache_from_source(*a, **kw):
    raise ValueError  # disable cache


builtins.exec = new_exec
builtins.compile = new_compile
sys.dont_write_bytecode = True


def test():
    code = """
# $SYM_FROM OS os name
def test():
    # $IF OS == "nt"
    print('Windows')
    # $ELIF OS == "posix"
    print('Linux')
    # $ELSE
    print('Unknown')
    # $ENDIF
    print(__SYM_OS)

test()
    """
    # print(preprocess(code))
    exec(code)


if __name__ == '__main__':
    test()
