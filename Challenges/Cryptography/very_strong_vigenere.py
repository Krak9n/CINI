#!/usr/bin/env python3
# The Mad Doctor: https://www.cipherchallenge.org/wp-content/uploads/2020/12/Five-ways-to-crack-a-Vigenere-cipher.pdf
from math import log
alphabet = map(chr, range(ord('a'), ord('z') + 1))
def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        p = alphabet.index(ciphertext[i])
        k = alphabet.index(key[i%len(key)])
        c = (p - k) % 26
        plaintext += alphabet[c]
    return plaintext

ciphertext = "fzau{ncn_isors_cviovw_pwcqoze}"
# implementation not finished. might return!
