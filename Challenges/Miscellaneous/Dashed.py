#!/usr/bin/env python3
from base64 import b64decode
from MorseCodePy import decode

def encrypt(string, length):
    return ' '.join(string[i:i+length] for i in range(0,len(string),length))

def binary_to_string(bits):
    return ''.join([chr(int(i, 2)) for i in bits])

"""
Raw-ASS Ceaser.
"""
def im(data, key):
    r = ""
    for c in data:
        if c.isalpha():
            shift = -key 
            if c.islower():
                r += chr(((ord(c) - ord('a') + shift) % 26) + ord('a'))
            else:
                r += chr(((ord(c) - ord('A') + shift) % 26) + ord('A'))
        else:
            r += c
    return r

def ceaser(data):
    for i in range(26):
        d = im(data, i)
        print(d)
        if "flag{" in d:
            break

with open("dashed.txt", "r") as file:
    data = file.read()
    file.close()
dec = str(bytes.fromhex(str(decode(data, language='english').replace("0x", "").replace(",", " "))).decode())
dec = encrypt(dec, 8).split()
print(ceaser(b64decode(binary_to_string(dec)).decode()))
