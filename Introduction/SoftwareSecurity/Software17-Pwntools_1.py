#!/usr/bin/env python3
from pwn import *
conn = remote("software-17.challs.olicyber.it", 13000)
conn.sendlineafter(b'iniziare ...', b'a')
print(conn.recvuntil(b"numeri\n"))
numbers = list(conn.recvline())
print(conn.sendafter(b": ", str(sum(numbers)).encode()))
conn.sendline()
print(conn.recvline())
