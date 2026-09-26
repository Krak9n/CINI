#!/usr/bin/env python3
from pwn import *
import json
import base64
import binascii
r = remote("based.challs.olicyber.it", 10600)
r.recvuntil(b'la tua risposta\n\n')
while True:
    mode = r.recvline().decode().split()
    print(mode)
    data = r.recvline().decode()
    if len(mode) >= 10:
        print(data)
        for o in data.split(" "):
            print(chr(int(o, 8)), end="")
        break
    d = json.loads(data)
    print(data)
    print(r.recvline())
    if "da" in mode[2] and "esadecimale" in mode[3]:
        r.sendline(str(json.dumps({"answer": bytes.fromhex(d['message']).decode()})).encode())
    elif "a" in mode[2] and "esadecimale" in mode[3]:
        r.sendline(str(json.dumps({"answer": d['message'].encode().hex()})).encode())
    elif "da" in mode[2] and "base64" in mode[3]:
        r.sendline(str(json.dumps({"answer": base64.b64decode(d['message']).decode()})).encode())
    elif "a" in mode[2] and "base64" in mode[3]:
        r.sendline(str(json.dumps({"answer": base64.b64encode(d['message'].encode()).decode()})).encode())
    elif "da" in mode[2] and "binario" in mode[3]: 
        n = int(d['message'], 2)
        r.sendline(str(json.dumps({"answer": n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()})).encode())
    elif "a" in mode[2] and "binario" in mode[3]:
        r.sendline(str(json.dumps({"answer": bin(int.from_bytes(d['message'].encode(), 'big')).replace("0b", "")})).encode())
    print(r.recvline())
    print(r.recvline())
    print(r.recvline())
