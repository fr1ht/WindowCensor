#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import NoReturn
import Xlib
from Xlib import display, X
from PIL import Image

from cfg import get_monitor_resolution


class Window:

  def __init__(self):
    self.resolution = get_monitor_resolution()
    self.display = display.Display()
    self.screen = self.display.screen()
    self.root_window = self.screen.root
    self.censor_window = self.root_window.create_gc(
      foreground=self.screen.black_pixel, background=self.screen.black_pixel
    )

  def get_image(self):
    """Get image by window resolutions
    """
    raw_image = self.root_window.get_image(
      0, 0, self.resolution.w, self.resolution.h, X.ZPixmap, 0xffffffff
    )
    return Image.frombytes(
      "RGB", (self.resolution.w, self.resolution.h), raw_image.data, "raw", "BGRX"
    )

  def censor(self, coordinates: tuple = (100, 100, 500, 500)) -> NoReturn:
    """Draw rectangle by &coordinates
    """
    self.root_window.fill_rectangle(self.censor_window, *coordinates)
    self.display.flush()
