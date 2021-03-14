#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import NoReturn


def show_image(image) -> NoReturn:
  import matplotlib.pyplot as plt

  plt.imshow(image)
  plt.show()
