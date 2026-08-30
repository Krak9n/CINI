#!/usr/bin/env python3
import gzip
import binascii

data = []
with open("extracted_bytes.dat", "rb") as file:
    data = file.read()
    file.close()
    
print((gzip.decompress(bytearray(data))).decode('utf-8', errors='replace'))
