#!/usr/bin/env python3
from pwn import *
conn = remote("software-17.challs.olicyber.it", 13000)
conn.sendlineafter(b'iniziare ...', b'a')
for i in range(10):
    conn.recvline()
    numbers = [int(i) for i in conn.recvline().decode().replace("[", "").replace("]", "").replace(",", "").split()]
    conn.sendafter(b": ", str(sum(numbers)).encode())
    conn.sendline()
print(conn.recvline().decode())
