#!/usr/bin/env python3
"""
fl4g here is global uninitialized variable. Try to get the values yourself by decompiling code.
"""
fl4g = "66 6c 61 67 7b 75 6e 75 35 33 64 5f 76 34 72 35 5f 34 72 33 5f 35 37 31 31 5f 63 30 6d 70 31 6c 33 64 7d"
print(bytearray.fromhex(fl4g).decode())
