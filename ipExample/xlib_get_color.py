#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Xlib import display, X
from PIL import Image #PIL

def getColor(x,y):
    W, H = 1, 1
    dsp = display.Display()
    root = dsp.screen().root
    raw = root.get_image(x, y, W, H, X.ZPixmap, 0xffffffff)
    if isinstance(raw.data,str):
        bytes=raw.data.encode()
    else:
        bytes=raw.data
    image = Image.frombytes("RGB", (W, H), bytes, "raw", "BGRX")
    print(image.getpixel((0, 0)))
    time.sleep(0.01)


getColor(1920, 1080)
