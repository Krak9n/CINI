#!/usr/bin/env python3
"""
Another solution could be to edit manually hexdump with xxd or hexedit.
"""
from PIL import ImageSequence, Image
c = open("corrupted_file", "rb").read()
n = open("cor.gif", "wb")
n.write(b"GIF89a" + c[13:])
n.close()
i = 0
for im in ImageSequence.Iterator(Image.open("cor.gif")):
    i += 1
    im.save('{}.png'.format(i), format="PNG")
