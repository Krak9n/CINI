#!/usr/bin/env python3
from pwn import *
elf = ELF("./sw-19")
r = remote("software-19.challs.olicyber.it", 13002)
r.sendlineafter(b"iniziare ...", b'')
for _ in range(20):
    target = r.recvuntil(b':').decode().replace("-> ", "").replace(":", "").strip()
    print(target + ": " + hex(elf.functions[target].address))
    r.sendline(str(hex(elf.functions[target].address)).encode())
print(r.recvline().decode())
