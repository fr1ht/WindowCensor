#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Xlib
from Xlib import display, X   # X is also needed
from PIL import Image #PIL
import time


def snapshot(filename="tmp.png"):
  """
  Take a screenshot and save it to `tmp.png` filename by default

  Args:
      filename: name of file where to store the screenshot

  Returns:
      display the screenshot

  """
  # w, h = self.get_current_resolution()
  w, h = (1920, 1080)
  dsp = display.Display()
  root = dsp.screen().root

  cnt = 0

  while True:
    raw = root.get_image(0, 0, w, h, X.ZPixmap, 0xffffffff)
    image = Image.frombytes("RGB", (w, h), raw.data, "raw", "BGRX")
    image.save(f"{cnt}_{filename}")
    time.sleep(1)
    cnt += 1

snapshot()
