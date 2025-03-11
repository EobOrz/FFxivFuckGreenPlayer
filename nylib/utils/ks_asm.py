from . import pip

pip.required('setuptools', 'keystone-engine', 'capstone')

import keystone
import capstone


def comp(code, address, data=None, resolves=None, arch=keystone.KS_ARCH_X86, mode=keystone.KS_MODE_64):
    _resolves = {}
    if resolves:
        for k, v in resolves.items():
            if isinstance(k, str): k = k.encode('ascii')
            assert isinstance(v, int)
            _resolves[k] = v

    ks = keystone.Ks(arch, mode)

    def resolver(key, p_value):
        if key in _resolves:
            p_value[0] = _resolves[key]
            return True
        return False

    ks.sym_resolver = resolver
    return ks.asm(code, address, True)[0]
