#!/usr/bin/env python3
"""
That was quite a stupid challenge but I did waste a lot of time on it.
"""
key = "b2 30 bd dc 10 7a e1 7b 2c 3b e2 ec 99 01".strip()
flag = "d4 5c dc bb 6b 1e d3 4a 4a 5e d2 df ac 7c".strip()
def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

print(xor(bytes.fromhex(key),bytes.fromhex(flag)).decode())
