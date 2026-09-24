#!/usr/bin/env python3
# If you want to learn more: https://mathmonks.com/modular-arithmetic
from pwn import *
r = remote("crypto-08.challs.olicyber.it", 30001)
print(r.recvuntil(b'\n\n'))
g = r.recvuntil(b'? ').decode().replace(" = ? ", "").split()
r.sendline(str(int(g[0]) % int(g[2])).encode())
print(r.recvline())
"""
And then just do some basic python operations. For example:
470 == 487 (mod 63)? (si/no) is no, because, 470 % 63 = 29
"""
