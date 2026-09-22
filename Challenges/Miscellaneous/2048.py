#!/usr/bin/env python3
from pwn import *
r = remote("2048.challs.olicyber.it", 10007)
print(r.recvuntil(b':\n'))
for _ in range(2048):
    v = r.recv(40).decode().strip().split()
    a = int(v[1])
    b = int(v[2])
    if v[0] == "PRODOTTO":
        r.sendline(str(a * b).encode())
    elif v[0] == "SOMMA":
        r.sendline(str(a + b).encode())
    elif v[0] == "DIFFERENZA":
        r.sendline(str(a - b).encode())
    elif v[0] == "POTENZA":
        r.sendline(str(a ** b).encode())
    elif v[0] == "DIVISIONE_INTERA":
        r.sendline(str(a // b).encode())
print(r.recvline().decode())
