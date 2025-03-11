from ..utils.pip import required
required('setuptools', 'keystone-engine', 'capstone')

import re
import struct
import typing

import capstone
import keystone

if typing.TYPE_CHECKING:
    from ..process import Process

ks_ = keystone.Ks(keystone.KS_ARCH_X86, keystone.KS_MODE_64)
cs_ = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64)


def read_code(p: 'Process', a, min_size=1, min_line=0, cs=None) -> tuple[list[capstone.CsInsn], int]:
    cs = cs or cs_
    ret = []
    proceed = 0
    disasm = cs.disasm(p.read(a, max(min_size + 0x10, 0x100)), a)
    out_of_code = False
    while proceed < min_size or len(ret) < min_line:
        if (i := next(disasm, None)) is None:
            disasm = cs.disasm(p.read(a + proceed, 0x100), a + proceed)
            continue
        if not out_of_code:
            if i.mnemonic == 'int3':
                out_of_code = True
        else:
            if i.mnemonic != 'int3':
                raise ValueError(f'Code at {a + proceed:#x} cross to another function')
        ret.append(i)
        proceed += i.size
    return ret, proceed


def create_inline_hook(p: 'Process', a, hook_bytes, entrance_offset=0, skip_original=0):
    try:
        alloc = p.alloc_near(0x1000, a)
        code_start = alloc + entrance_offset
        jump_code = b'\xe9' + struct.pack('<i', code_start - a - 5)  # jmp alloc
    except ValueError:
        alloc = p.alloc(0x1000)
        code_start = alloc + entrance_offset
        jump_code = b'\xff\x25\x00\x00\x00\x00' + struct.pack('<Q', code_start)  # jmp qword ptr [rip];dq alloc

    orig_codes, orig_size = read_code(p, a, min_size=len(jump_code), min_line=skip_original)
    if (pad := orig_size - len(jump_code)) > 0: jump_code += b'\x90' * pad

    return_at = a + len(jump_code)
    hook_bytes_ = hook_bytes
    for i in orig_codes[skip_original:]:
        # todo: rebuild relative address
        hook_bytes_ += i.bytes
    hook_bytes_ += b'\xff\x25\x00\x00\x00\x00' + struct.pack('<Q', return_at)  # jmp qword ptr [rip];dq return_at
    p.write(alloc, b'\0' * entrance_offset + hook_bytes_)
    return alloc, jump_code, b''.join(i.bytes for i in orig_codes)


def inline_hook(p: 'Process', a, hook_bytes, entrance_offset=0, skip_original=0):
    alloc, jump_code, orig_code = create_inline_hook(p, a, hook_bytes, entrance_offset, skip_original)
    p.write(a, jump_code)
    # to restore, free(alloc) and write orig_code to a
    return alloc, orig_code


def asm(code, addr=0, data_size=0, ks=None, cs=None):
    codes = [l_ for l_ in (l.strip() for l in re.split(r'[\n;\r]', code)) if l_]
    counter = 0
    inst_count = 0
    inst2lbl = {}
    for i in range(len(codes)):
        line = codes[i]
        if m := re.match(r"(\w+):", line):  # label
            inst2lbl.setdefault(inst_count, []).append(m.group(1))
            continue
        inst_count += 1
        if m := re.search(r'\W(__data__)\W', line):
            counter = (id_ := counter) + 1
            prepend_lbl = f'__read_data_{id_}__'
            # replace __data__ with rip-prepend_lbl+start-data_size
            codes[i] = line[:m.start(1)] + f'(rip-{prepend_lbl}+__start__-{data_size:#x})' + line[m.end(1):] + f';{prepend_lbl}:'
    bytecode = (ks or ks_).asm('__start__:;' + ';'.join(codes), addr, True)[0]
    labels = {}
    if inst2lbl:
        for i, inst in enumerate((cs or cs_).disasm(bytecode, addr)):
            if i in inst2lbl:
                for lbl in inst2lbl.pop(i):
                    labels[lbl] = inst.address
                if not inst2lbl:
                    break
    return bytecode, labels


class InlineHook:
    alloc_at = 0
    hook_code = b''
    orig_code = b''

    def __init__(self, process: 'Process', code, addr, data_size=0, skip_original=0):
        self.process = process
        if isinstance(code, bytes):
            self.code = code
            self.labels = {}
        else:
            self.code, self.labels = asm(code, addr, data_size)
        self.addr = addr
        self.data_size = data_size
        self.skip_original = skip_original

        self._enabled = False

    @property
    def data_at(self):
        self.alloc()
        return self.alloc_at

    @property
    def code_at(self):
        self.alloc()
        return self.alloc_at + self.data_size

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if (value := bool(value)) == self._enabled: return
        self.alloc()
        if value:
            self.process.write(self.addr, self.hook_code)
        else:
            self.process.write(self.addr, self.orig_code)
        self._enabled = value

    def alloc(self):
        if not self.alloc_at:
            self.alloc_at, self.hook_code, self.orig_code = create_inline_hook(self.process, self.addr, self.code, self.data_size, self.skip_original)

    def free(self):
        if self.alloc_at:
            if self._enabled:
                self.process.write(self.addr, self.orig_code)
                self._enabled = False
            self.process.free(self.alloc_at, 0x1000)
            self.alloc_at = 0
            self.hook_code = b''
            self.orig_code = b''

    def __del__(self):
        self.free()
