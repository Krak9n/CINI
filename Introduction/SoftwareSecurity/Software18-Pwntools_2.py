#!/usr/bin/env python3
from pwn import *
r = remote("software-18.challs.olicyber.it", 13001)
r.sendlineafter(b"iniziare ...", b'a')
for _ in range(100):
    r.recvuntil(b"restituiscimi ")
    values = r.recvline().decode().split()
    print(values)
    does = values[1]
    v = int(values[0].replace("0x",""), base=16)
    ind = int(values[3].replace("-bit",""))
    if does == "packed" and ind == 64:
        r.sendafter(b" Result : ", p64(v))
    elif does == "packed" and ind == 32:
        r.sendafter(b" Result : ", p32(v))
    elif does == "unpacked" and ind == 64:
        r.sendafter(b" Result : ", u64(v))
    elif does == "unpacked" and ind == 32:
        r.sendeafter(b" Result : ", u32(v))
print(r.recvline().decode())
