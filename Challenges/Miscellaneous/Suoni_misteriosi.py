#!/usr/bin/env python3
from MorseCodePy import decode
# This library: https://pypi.org/project/MorseCodePy/
# And the text was exported from the provided audio file.
code = ".--. .-. .. ... . -. -.-. --- .-.. .. -. . -. ... .. -. .- .. -. -.-. .. ..- ... --- .-.."
print("flag{"+decode(code, language="english").lower()+"}")
