#!/usr/bin/env python3
from pwn import *
conn = remote("software-17.challs.olicyber.it", 13000)
conn.sendlineafter(b'iniziare ...', b'a')
for i in range(10):
    print(conn.recvuntil(b"numeri\n"))
    numbers = list(conn.recvline())
    print(numbers)
    print(sum(numbers))
    print(conn.recvline())
    print(conn.sendlineafter(b": ", str(sum(numbers)).encode()))
    print(conn.recvline())
