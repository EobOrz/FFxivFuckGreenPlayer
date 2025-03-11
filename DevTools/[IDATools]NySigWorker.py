from idc import *
from idaapi import *
from idautils import *
import tkinter as tk

min_ea = inf_get_min_ea()
max_ea = inf_get_max_ea()
hex_char = [f'{i:02x} ' for i in range(256)] + ['* ', '? ']


# region make sig

def ea_point(ea):
    return next(v for v in (get_operand_value(ea, i) for i in range(2)) if min_ea < v < max_ea)


def line_sig(ea, mask_op=False):
    decode_insn(insn := ida_ua.insn_t(), ea)
    size = insn.size
    line = get_bytes(ea, size)
    offset_op = next((max(op.offb, 1) for op in insn.ops), len(line))
    if mask_op:
        try:
            mask_idx = next(i for i in range(2) if min_ea < get_operand_value(ea, i) < max_ea)
        except StopIteration:
            print(f"[!]cant find operand at {ea:x}, with operand value {get_operand_value(ea, 0):x} {get_operand_value(ea, 1):x}")
            raise
        mask_start = insn.ops[mask_idx].offb
        mask_end = insn.ops[mask_idx + 1].offb or size
    else:
        mask_start = mask_end = size
    res = "".join(hex_char[b] for b in line[:offset_op])
    for i in range(offset_op, size):
        res += '* ' if mask_start <= i < mask_end else '? '
    return res


def sig_search(sig: str, max_search_cnt: int = 10):
    addr = min_ea
    while max_search_cnt > 0:
        addr = find_binary(addr, max_ea, sig, 16, SEARCH_DOWN | SEARCH_NEXT)
        if addr == BADADDR: break
        yield addr
        max_search_cnt -= 1


def find_xrefs(ea: int) -> dict:
    xrefs = {}
    for xref in XrefsTo(ea, 0):
        xrefs.setdefault(xref.type, []).append(xref.frm)
    return xrefs


fl_name = {
    dr_O: 'dr_O',
    dr_I: 'dr_I',
    dr_R: 'dr_R',
    dr_T: 'dr_T',
    dr_W: 'dr_W',
    dr_S: 'dr_S',
    fl_CF: 'fl_CF',
    fl_CN: 'fl_CN',
    fl_JF: 'fl_JF',
    fl_JN: 'fl_JN',
    fl_F: 'fl_F',
}


def is_only_ref_from(from_, to):
    found = False
    for xref in XrefsTo(to, 0):
        if xref.frm == from_:
            found = True
        elif xref.type in (ida_xref.fl_CF, ida_xref.fl_CN, ida_xref.fl_JF, ida_xref.fl_JN, ida_xref.fl_F):
            return False
    return found


def is_only_ref_to(from_, to):
    found = False
    import ida_xref
    for xref in XrefsFrom(from_, 0):
        # print(xref, fl_name.get(xref.type), hex(xref.to),xref.iscode,xref.user)
        if xref.to == to:
            found = True
        elif xref.type in (ida_xref.fl_CF, ida_xref.fl_JF, ida_xref.fl_JN, ida_xref.fl_F):
            return False
    return found


class SigSearch:
    SUCCESS = 0
    FAIL = -1
    FORWARD = 1
    BACKWARD = 2
    PARENT = 3

    def __init__(self, start_ea, mgr: 'SigSearcher'):
        self.mgr = mgr
        self.start_ea = start_ea
        self.current_ea = start_ea
        if not (func := get_func(start_ea)):
            raise ValueError(f"no function at {start_ea:x}")
        self.func_range = range(func.start_ea, func.end_ea)
        self.state = SigSearch.FORWARD
        self.sigs = [line_sig(self.current_ea)]
        self.offset = 0
        self.inst_offset = 0

    def walk(self):
        if self.state == SigSearch.FORWARD:
            self.walk_forward()
        if self.state == SigSearch.BACKWARD:
            self.walk_backward()
        self.test()

    def walk_forward(self):
        next_ea = next_head(self.current_ea, self.func_range.stop)
        if next_ea not in self.func_range or not is_only_ref_from(self.current_ea, next_ea):
            self.state = SigSearch.BACKWARD
            self.current_ea = self.start_ea
            return
        self.sigs.append(line_sig(next_ea))
        self.current_ea = next_ea

    def walk_backward(self):
        next_ea = prev_head(self.current_ea, self.func_range.start)
        if next_ea not in self.func_range or not is_only_ref_to(next_ea, self.current_ea):
            # print(f"[!]fail at {self.current_ea:x} to {next_ea:x} {next_ea not in self.func_range=} {not is_only_ref_to(next_ea, self.current_ea)=}")
            self.state = SigSearch.FAIL
            return
        self.sigs.insert(0, line_sig(next_ea))
        self.offset += self.current_ea - next_ea
        self.inst_offset += 1
        self.current_ea = next_ea

    sig = property(lambda self: "".join(self.sigs))

    def test(self):
        if self.state == SigSearch.FAIL or self.state == SigSearch.SUCCESS: return
        matches = list(sig_search(self.sig, 2))
        if len(matches) == 1:
            self.state = SigSearch.SUCCESS
        elif len(matches) == 0:
            self.state = SigSearch.FAIL  # should not happen

    def count_match(self, max_=10):
        return sum(1 for _ in sig_search(self.sig, max_))

    def make(self, mask_addr=False):
        count_match = self.count_match()
        if count_match < 10:
            while len(self.sigs) - 1 > self.inst_offset:
                if sum(1 for _ in sig_search("".join(self.sigs[:-1]), count_match + 1)) == count_match:
                    self.sigs.pop()
                else:
                    break
        if mask_addr:
            self.sigs[self.inst_offset] = line_sig(self.start_ea, True)
        res = self.sig
        if self.offset:
            res += f' +{self.offset:#x}'
        return res


class SigSearcher:
    def __init__(self, target_ea, max_workers=500):
        self.target_ea = target_ea
        self.max_workers = max_workers
        self.workers = []
        if get_func(target_ea):
            self.workers.append(SigSearch(target_ea, self))
        for xref in XrefsTo(target_ea, 0):
            if xref.type in (fl_CF, fl_CN, fl_JF, fl_JN, dr_R, dr_W, dr_T):
                try:
                    worker = SigSearch(xref.frm, self)
                except ValueError:
                    continue
                if not self.append(worker): break

        self.found = []
        self.failed = []

    def append(self, worker):
        if len(self.workers) < self.max_workers:
            self.workers.append(worker)
            return True
        return False

    def walk(self):
        for worker in self.workers:
            if worker.state > 0:
                worker.walk()
            if worker.state <= 0:
                self.workers.remove(worker)
                if worker.state == SigSearch.SUCCESS:
                    self.found.append(worker)
                else:
                    self.failed.append(worker)

    def auto_walk(self, max_found=10, max_step=50) -> tuple[int, list[SigSearch]]:
        if not self.workers:
            raise ValueError("no workers")
        for _ in range(max_step):
            self.walk()
            if len(self.workers) == 0: break
            if len(self.found) >= max_found: break
        if not self.found:
            sorted_workers = sorted(self.failed + self.workers, key=lambda w: w.count_match())
            min_match = sorted_workers[0].count_match()
            workers = []
            for worker in sorted_workers:
                if worker.count_match() == min_match:
                    workers.append(worker)
                else:
                    break
        else:
            min_match = 1
            workers = self.found
        return min_match, workers


def make_sig(target):
    try:
        searcher = SigSearcher(target)
        print(f"[.]start search {target:x} {get_name(target)} in {len(searcher.workers)} ea")
        min_match, found = searcher.auto_walk()
        print(f"[+]found {len(found)} sig with {min_match} min match")
        for worker in found:
            try:
                print(f"[+] {worker.start_ea:x} : {worker.make(worker.start_ea != target)}")
            except Exception as e:
                print(f"[!]error when make sig {worker.start_ea:x}: {e}")
                print(traceback.format_exc())
    except Exception as e:
        print(f"[!]error when search {target:x} {get_name(target)}: {e}")
        print(traceback.format_exc())


# endregion

# region search sig

def get_exec_data():
    import sys
    import types
    if '__exec_cache__' not in sys.modules:
        sys.modules['__exec_cache__'] = m = types.ModuleType('__exec_cache__')
        m.data = get_bytes(inf_get_min_ea(), inf_get_max_ea() - inf_get_min_ea())
    return sys.modules['__exec_cache__'].data


# xx xx xx xx 空格分割
# [xx:yy] 单字节从 xx 到 yy
# [xx|yy|zz] 单字节 xx 或 yy 或 zz
# ? ? ? ? 视作变量（默认不储存）
# ^ ^ ^ ^ 视作字串（默认储存）
# * * * * 视作跳转（默认储存）
# ?{n} / *{n} 视作匹配n次
# ?{n:m} / *{n:m} 视作匹配n-m次
# (xx xx xx xx) 不存储的分组
# <xx xx xx xx> 储存的分组
# <* * * *: yy yy yy yy> 对分组数据二级匹配
# <* * * *: yy yy yy yy <* * * *:zz zz zz zz>> 对分组数据多级匹配，仅适用于跳转
import io
import re
import typing

fl_is_ref = 1 << 0
fl_is_byes = 1 << 1
fl_store = 1 << 2

hex_chars = set(b'0123456789abcdefABCDEF')
dec_chars = set(b'0123456789')

special_chars_map = {i for i in b'()[]{}?*+-|^$\\.&~# \t\n\r\v\f'}


def take_dec_number(pattern: str, i: int):
    assert i < len(pattern) and ord(pattern[i]) in dec_chars
    j = i + 1
    while j < len(pattern) and ord(pattern[j]) in dec_chars:
        j += 1
    return int(pattern[i:j]), j


def take_cnt(pattern: str, i: int, regex_pattern: bytearray):
    if i < len(pattern) and pattern[i] == '{':
        regex_pattern.append(123)  # {
        n1, i = take_dec_number(pattern, i + 1)
        regex_pattern.extend(str(n1).encode())
        if pattern[i] == ':':
            n2, i = take_dec_number(pattern, i + 1)
            assert n1 <= n2
            regex_pattern.append(44)  # ,
            regex_pattern.extend(str(n2).encode())
        assert pattern[i] == '}'
        regex_pattern.append(125)  # }
        i += 1
    return i


def take_byte(pattern: str, i: int, regex_pattern: bytearray):
    assert i + 2 <= len(pattern)
    next_byte = int(pattern[i:i + 2], 16)
    if next_byte in special_chars_map:
        regex_pattern.append(92)  # \
    regex_pattern.append(next_byte)
    return i + 2


def _take_unk(pattern: str, i: int):
    start_chr = pattern[i]
    assert start_chr in ('?', '*', '^')
    if i + 1 < len(pattern) and pattern[i + 1] == start_chr:
        i += 1
    return start_chr, i + 1


def take_unk(pattern: str, i: int, regex_pattern: bytearray):
    start_unk, i = _take_unk(pattern, i)
    regex_pattern.append(46)
    i = take_cnt(pattern, i, regex_pattern)
    while i < len(pattern):
        match pattern[i]:
            case ' ':
                i += 1
            case c if c == start_unk:
                start_unk, i = _take_unk(pattern, i)
                regex_pattern.append(46)
                i = take_cnt(pattern, i, regex_pattern)
            case _:
                break
    return start_unk, i


def _compile_pattern(pattern: str, i=0, ret_at=None):
    _i = i
    regex_pattern = bytearray()
    sub_matches = []
    group_flags = []
    while i < len(pattern):
        match pattern[i]:
            case ' ':
                i += 1
            case '[':
                regex_pattern.append(91)  # [
                i += 1
                i = take_byte(pattern, i, regex_pattern)
                while True:
                    match pattern[i]:
                        case ' ':
                            i += 1
                        case ']':
                            regex_pattern.append(93)  # ]
                            i += 1
                            break
                        case '|':
                            i = take_byte(pattern, i + 1, regex_pattern)
                        case ':':
                            regex_pattern.append(45)  # -
                            i = take_byte(pattern, i + 1, regex_pattern)
                        case c:
                            raise ValueError(f'Invalid character {c} in pattern {pattern!r} at {i}')

            case '(':
                base_flag = 0  # not fl_store
                regex_pattern.append(40)  # (
                unk_type, i = take_unk(pattern, i + 1, regex_pattern)
                if unk_type == '*':
                    base_flag |= fl_is_ref
                elif unk_type == '^':
                    base_flag |= fl_is_byes
                sub_pattern = None
                while True:
                    match pattern[i]:
                        case ' ':
                            i += 1
                        case ')':
                            regex_pattern.append(41)  # )
                            i += 1
                            break
                        case ':':
                            sub_pattern, i = _compile_pattern(pattern, i + 1, ret_at=')')
                            assert pattern[i] == ')', f'Expected ) get {pattern[i]} at {i} in pattern {pattern!r}'
                            regex_pattern.append(41)
                            i += 1
                            break
                        case c:
                            raise ValueError(f'Invalid character {c} in pattern {pattern!r} at {i}')
                group_flags.append(base_flag)
                sub_matches.append(sub_pattern)
            case '<':
                base_flag = fl_store
                regex_pattern.append(40)
                unk_type, i = take_unk(pattern, i + 1, regex_pattern)
                if unk_type == '*':
                    base_flag |= fl_is_ref
                elif unk_type == '^':
                    base_flag |= fl_is_byes
                sub_pattern = None
                while True:
                    match pattern[i]:
                        case ' ':
                            i += 1
                        case '>':
                            regex_pattern.append(41)
                            i += 1
                            break
                        case ':':
                            sub_pattern, i = _compile_pattern(pattern, i + 1, ret_at='>')
                            assert pattern[i] == '>', f'Expected > get {pattern[i]} at {i} in pattern {pattern!r}'
                            regex_pattern.append(41)
                            i += 1
                            break
                        case c:
                            raise ValueError(f'Invalid character {c} in pattern {pattern!r} at {i}')
                group_flags.append(base_flag)
                sub_matches.append(sub_pattern)
            case '?' | '*' | '^' as c:
                regex_pattern.append(40)
                unk_type, i = take_unk(pattern, i, regex_pattern)
                regex_pattern.append(41)
                if c == '?':
                    group_flags.append(0)
                elif c == '*':
                    group_flags.append(fl_is_ref | fl_store)
                elif c == '^':
                    group_flags.append(fl_is_byes | fl_store)
                else:
                    raise ValueError(f'Invalid character {c} in pattern {pattern!r} at {i}')
                sub_matches.append(None)
            case c if ord(c) in hex_chars:
                i = take_byte(pattern, i, regex_pattern)
                i = take_cnt(pattern, i, regex_pattern)
            case c if c == ret_at:
                break
            case c:
                fmt_pattern = pattern[:i] + '_' + pattern[i] + '_' + pattern[i + 1:]
                raise ValueError(f'Invalid character {c} in pattern {fmt_pattern!r} at {i} (ret_at={ret_at})')
    try:
        regex = re.compile(bytes(regex_pattern), re.DOTALL)
    except re.error as e:
        raise ValueError(f'{e}: ({pattern!r}, {_i}, {ret_at!r}) -> {bytes(regex_pattern)}')
    return Pattern(regex, sub_matches, group_flags, pattern), i


def compile_pattern(pattern: str):
    return _compile_pattern(pattern)[0]


class Pattern:
    def __init__(self, regex: re.Pattern, sub_matches: 'typing.List[None | Pattern]', group_flags, pattern: str):
        self.regex = regex
        self.sub_matches = sub_matches
        self.group_flags = group_flags
        self.pattern = pattern
        self.res_is_ref = []
        for i, (sub, flag) in enumerate(zip(sub_matches, group_flags)):
            if flag & fl_store:
                self.res_is_ref.append(flag & fl_is_ref)
            if sub is not None:
                self.res_is_ref.extend(sub.res_is_ref)

    def finditer(self, _data: bytes | bytearray | memoryview, ref_base=0):
        data = _data if isinstance(_data, memoryview) else memoryview(_data)
        for match in self.regex.finditer(data):
            res = []
            if self._parse_match(data, match, res, ref_base):
                yield match.start(0), res

    def _parse_match(self, data: memoryview, match: re.Match, res: list, ref_base=0):
        for i, (sub_match, flag) in enumerate(zip(self.sub_matches, self.group_flags)):
            if flag & fl_is_byes:
                res.append(match.group(i + 1))
            else:
                val = int.from_bytes(match.group(i + 1), 'little', signed=True)
                if flag & fl_is_ref:
                    val += match.end(i + 1)
                if flag & fl_store:
                    res.append(val)
                if sub_match is not None:
                    start = val if flag & fl_is_ref else val - ref_base
                    if start < 0 or start >= len(data):
                        return False
                    if not sub_match._match(data, start, res, ref_base):
                        return False
        return True

    def _match(self, _data: memoryview, start_at: int, res: list, ref_base=0):
        if not (match := self.regex.match(_data, start_at)): return False
        return self._parse_match(_data, match, res, ref_base)

    def fmt(self, ind: str | int = ' ', _ind=0):
        if isinstance(ind, int): ind = ' ' * ind
        s = io.StringIO()
        s.write(ind * _ind)
        s.write(fmt_bytes_regex_pattern(self.regex.pattern))
        s.write('\n')
        s.write(ind * _ind)
        s.write('res is ref:')
        for flag in self.res_is_ref:
            s.write(' ref' if flag else ' val')
        s.write('\n')
        for i, (sub, flag) in enumerate(zip(self.sub_matches, self.group_flags)):
            s.write(ind * _ind)
            s.write(f'{i}:{"ref" if flag & fl_is_ref else "val"}{" store" if flag & fl_store else ""}\n')
            if sub is not None:
                s.write(sub.fmt(ind, _ind + 1))
                s.write('\n')
        return s.getvalue().rstrip()


def fmt_bytes_regex_pattern(pat: bytes):
    s = ''
    is_escape = False
    is_in_bracket = 0
    for b in pat:
        if is_escape:
            is_escape = False
            s += f'\\x{b:02x}'
        elif b == 92:  # \
            is_escape = True
        elif b in special_chars_map:
            if b == 123:  # {
                is_in_bracket += 1
            elif b == 125:  # }
                is_in_bracket -= 1
            s += chr(b)
        elif is_in_bracket:
            s += chr(b)
        else:
            s += f'\\x{b:02x}'
    return s


class IPatternScanner:
    def search(self, pattern: str | Pattern) -> typing.Generator[tuple[int, list[int]], None, None]:
        raise NotImplementedError

    def search_unique(self, pattern: str | Pattern) -> tuple[int, list[int]]:
        s = self.search(pattern)
        try:
            res = next(s)
        except StopIteration:
            raise KeyError('pattern not found')
        try:
            next(s)
        except StopIteration:
            return res
        raise KeyError('pattern is not unique, at least 2 is found')

    def find_addresses(self, pattern: str | Pattern):
        for address, _ in self.search(pattern):
            yield address

    def find_vals(self, pattern: str | Pattern):
        for address, args in self.search(pattern):
            yield args

    def find_address(self, pattern: str | Pattern):
        return self.search_unique(pattern)[0]

    def find_val(self, pattern: str | Pattern):
        return self.search_unique(pattern)[1]


class IdaScanner(IPatternScanner):
    def __init__(self):
        self.data = get_exec_data()
        self.min_ea = inf_get_min_ea()

    def search(self, pattern: str | Pattern) -> typing.Generator[tuple[int, list[int]], None, None]:
        if isinstance(pattern, str):
            pattern = compile_pattern(pattern)
        for address, args in pattern.finditer(self.data):
            yield self.min_ea + address, [a + self.min_ea if r else a for a, r in zip(args, pattern.res_is_ref)]


def search_sig(sig: str):
    res = list(IdaScanner().search(sig))
    print(f"[+] {len(res)} found for sig {sig}")
    for ea, args in res:
        print(f"[+] {ea:#x}: " + ", ".join(f"{a:#x}" for a in args))


# endregion

def main():
    def call_then_close(func, *args):
        def f():
            try:
                func(*args)
            finally:
                root.destroy()

        return f

    root = tk.Tk()
    root.title("NySigWorker")

    frame_func1 = tk.LabelFrame(root, text="make sig", padx=5, pady=5)
    frame_func2 = tk.LabelFrame(root, text="search sig", padx=5, pady=5)
    frame_buttons = tk.Frame(root, padx=5, pady=5)

    frame_func1.pack(padx=10, pady=5, fill="x")
    frame_func2.pack(padx=10, pady=5, fill="x")
    frame_buttons.pack(padx=10, pady=5, fill="x")

    # Components for func1
    suggestion = []
    if (_here := here()) != BADADDR:
        suggestion.append(_here)
        try:
            suggestion.append(ea_point(_here))
        except StopIteration:
            pass

    entry_manual_input = tk.Entry(frame_func1)
    button_exec_func1 = tk.Button(frame_func1, text="exec", command=call_then_close(lambda: make_sig(eval(entry_manual_input.get()))))
    for i, s in enumerate(suggestion):
        tk.Button(frame_func1, text=get_name(s) or f'ea_{s:x}', command=call_then_close(make_sig, s)).grid(row=0, column=i)
    entry_manual_input.grid(row=1, column=0, sticky="ew", columnspan=max(len(suggestion), 1))
    button_exec_func1.grid(row=1, column=max(len(suggestion), 1), sticky="ew")

    frame_func1.columnconfigure(0, weight=1)

    # Components for func2
    entry_input_func2 = tk.Entry(frame_func2)
    button_exec_func2 = tk.Button(frame_func2, text="exec", command=call_then_close(lambda: search_sig(entry_input_func2.get())))

    entry_input_func2.grid(row=0, column=0, sticky="ew")
    button_exec_func2.grid(row=0, column=1)

    frame_func2.columnconfigure(0, weight=1)

    # Cancel Button
    button_cancel = tk.Button(frame_buttons, text="cancel", command=root.destroy)
    button_cancel.pack(side="right")

    root.mainloop()


class NySigFinder(plugin_t):
    flags = 0  # 插件类别 或者特性
    wanted_name = "NySigFinder"  # 展示名称
    wanted_hotkey = "Ctrl-Alt-S"  # 其快捷键
    comment = "sig finder"  # 插件描述
    help = "ask gpt if you need"  # 帮助信息

    # 初始化时运行的，可以判断是否要启用这个插件，比如你这个插件主要是针对x86的，
    # 那你就要判断当前分析的是不是x86，然后在决定是否要显示或者启用这个插件
    def init(self):
        return PLUGIN_KEEP

    # 插件退出时要做的操作，比如说你打开了某个文件，要到插件结束时才能关闭，
    # 这里就给你这个机会
    def term(self):
        pass

    # 按快捷键等 插件运行时 的地方
    def run(self, arg):
        main()


# 插件入口
def PLUGIN_ENTRY():
    return NySigFinder()


if __name__ == '__main__':
    NySigFinder().run(0)
