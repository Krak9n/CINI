#!/usr/bin/env python3
ciphertext = bytes.fromhex("104e137f425954137f74107f525511457f5468134d7f146c4c")
for key in range(256):
    plaintext = bytes(b ^ key for b in ciphertext)
    try:
        print(f"{key} -> "+str(plaintext.decode()))
    except UnicodeDecodeError:
        continue
