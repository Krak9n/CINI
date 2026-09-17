#!/usr/bin/env python3
"""
Bacon Cipher type shit.
"""
dic = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
          'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
          'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
          'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
          'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'}

def decrypt(text):
    res = ""
    for i in range(0, len(text) - 4, 5):
        sub = text[i:i+5]
        res += list(dic.keys())[list(dic.values()).index(sub)]
    return res

print(decrypt("AAAABAAAAAAAABAABBBAABBABABAAABAABABAABAABBBABAABBAAAAABAABABAABBBBAAA".lower()))
