import io

rand_engine = 'secrets'

match rand_engine:
    case 'os':
        import os

        randint = lambda a, b: a + int.from_bytes(os.urandom(((b - a).bit_length() + 7) // 8), 'little') % (b - a)
        randbytes = os.urandom
    case 'secrets':
        import secrets

        randint = lambda a, b: secrets.randbelow(b - a) + a
        randbytes = lambda n: secrets.token_bytes(n)
    case 'random':
        import random

        randint = random.randint
        randbytes = random.randbytes
    case _:
        raise ValueError('invalid rand engine')


def miller_rabin(p):
    if p == 1: return False
    if p == 2: return True
    if p % 2 == 0: return False
    m, k, = p - 1, 0
    while m % 2 == 0:
        m, k = m // 2, k + 1
    a = randint(2, p - 1)
    x = pow(a, m, p)
    if x == 1 or x == p - 1: return True
    while k > 1:
        x = pow(x, 2, p)
        if x == 1: return False
        if x == p - 1: return True
        k = k - 1
    return False


def is_prime(p, r=40):
    for i in range(r):
        if not miller_rabin(p):
            return False
    return True


def get_prime_by_max(_max):
    s_num = num = randint(_max // 2, _max)
    while True:
        if is_prime(num):
            return num
        elif num + 1 >= _max:
            break
        else:
            num += 1
    while True:
        if is_prime(s_num): return s_num
        s_num -= 1


def get_prime(bit_size):
    return get_prime_by_max(1 << bit_size)


class SimpRsa:
    def __init__(self, n=0, e=0, d=0):
        self.n, self.e, self.d = n, e, d
        self.default_size = (n.bit_length() + 7) // 8

    def encrypt(self, v: int | bytes):
        assert v < self.n, f'v={v:#x}, n={self.n:#x}'
        return pow(v, self.e, self.n)

    def decrypt(self, v: int | bytes):
        assert v < self.n, f'v={v:#x}, n={self.n:#x}'
        return pow(v, self.d, self.n)

    def encrypt_bytes(self, v: bytes, to_size=0):
        return self.encrypt(int.from_bytes(v, 'little')).to_bytes(to_size or self.default_size, 'little')

    def decrypt_bytes(self, v: bytes, to_size=0):
        return self.decrypt(int.from_bytes(v, 'little')).to_bytes(to_size or self.default_size, 'little')


class SimpleChipper:
    def __init__(self, n: int, e: int = -1, d: int = -1):
        self.n = n
        self.e = e
        self.d = d
        self.size = (n.bit_length() + 7) // 8
        self.check_size = self.size - 1
        if self.size >> 32 != 0:
            raise ValueError('n is too large')
        elif self.size >> 16 != 0:
            self.p_size = 4
        elif self.size >> 8 != 0:
            self.p_size = 2
        else:
            self.p_size = 1

    def pad(self, src: bytes):
        to_pad = self.check_size - len(src) % self.check_size
        if to_pad < self.p_size: to_pad += self.check_size
        return src + randbytes(to_pad - self.p_size) + to_pad.to_bytes(self.p_size, 'little')

    def unpad(self, src: bytes):
        return src[:-int.from_bytes(src[-self.p_size:], 'little')]

    def dec(self, src: bytes):
        if self.d == -1: raise ValueError('private key is not available')
        src_ = io.BytesIO(src)
        res = io.BytesIO()
        while data := src_.read(self.size):
            res.write(pow(int.from_bytes(data, 'little'), self.d, self.n).to_bytes(self.check_size, 'little'))
        return self.unpad(res.getvalue())

    def enc(self, src: bytes):
        if self.e == -1: raise ValueError('public key is not available')
        src_ = io.BytesIO(self.pad(src))
        res = io.BytesIO()
        while data := src_.read(self.check_size):
            res.write(pow(int.from_bytes(data, 'little'), self.e, self.n).to_bytes(self.size, 'little'))
        return res.getvalue()


def make_rsa_key(bit_size):
    p1, p2 = get_prime(bit_size), get_prime(bit_size)
    n = p1 * p2
    o = (p1 - 1) * (p2 - 1)
    e = get_prime_by_max(o)
    d = pow(e, -1, o)
    return n, e, d


def _rsa_test():
    p1, p2 = get_prime(64), get_prime(64)
    n = p1 * p2
    o = (p1 - 1) * (p2 - 1)
    e = get_prime_by_max(o)
    d = pow(e, -1, o)
    test_rsa = SimpRsa(n, e, d)
    print(f'n={n:#x},')
    print(f'e={e:#x},')
    print(f'd={d:#x},')
    print(hex(encr := test_rsa.encrypt(9)))
    print(hex(test_rsa.decrypt(encr)))
    print((encr := test_rsa.encrypt_bytes(b'test')).hex(' '))
    print(test_rsa.decrypt_bytes(encr))


if __name__ == '__main__':
    _rsa_test()
