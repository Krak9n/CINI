#!/usr/bin/env python3
"""
I am lazy. Here one should extract the frames and then just use stegsolve on frames to save the flag.
"""
from PIL import Image
num = 8
with Image.open('bel_paesaggio.gif') as im:
    for i in range(num):
        im.seek(im.n_frames // num * i)
        im.save('{}.png'.format(i))
