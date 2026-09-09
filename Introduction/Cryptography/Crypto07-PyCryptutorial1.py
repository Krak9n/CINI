#!/usr/bin/env python3
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import pwn

r = pwn.remote("crypto-07.challs.olicyber.it", 30000)
r.recvuntil(b"\n\n")
cip = r.recvline().decode().split()[2]
mode = r.recvline().decode().split()[2]
key = bytes.fromhex(r.recvline().decode().split()[2].replace("'", ""))
plaintext = str(r.recvline().decode().split("plaintext = ", 1)[1]).encode()
scheme = r.recvline().decode().split()[3]

# encrypt in hex
cipher = DES.new(key, DES.MODE_CBC)
cipher.encrypt(pad(plaintext, 8))
print(r.recvuntil(b'? '))
print(r.send(plaintext.hex().encode()))
print(r.recvline())
print(r.sendafter(b"$ ", cipher.iv.hex().encode()))
r.interactive()
