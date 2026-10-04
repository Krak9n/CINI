#!/usr/bin/env python3
data = "66 6d 63 64 7f 62 36 58 3c 61 39 6a 68 52 3a 61 74 4e 78 66 79 65 6b 17".split()
def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

print('f', end='')
for i in range(len(data)):
    print(xor(bytes.fromhex(data[i]), i.to_bytes((i.bit_length() + 7) // 8, 'big')).decode(), end='')

