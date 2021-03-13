#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import matplotlib.pyplot as plt
from PIL import Image, ImageFont, ImageDraw
import numpy as np
from collections import Counter


def show_image(image):
  plt.imshow(image)
  plt.show()


def create_image(size):
  return Image.new('RGB', size, 'white')


def get_size(size, text):
  width, height = size.split('x')

  height = int(height)

  if not width:
    width = len(text) * (7)

  return int(width), height


def main(font, size, text, file):
  x, y = (0, 0)
  size = get_size(size, text)
  new_image = create_image(size)

  if not font:
    font = 'FiraCode-Medium.ttf'

  font = ImageFont.truetype(font, size=size[1])
  draw = ImageDraw.Draw(new_image)

  color = 'black'

  draw.text((x, y), text, fill=color, font=font)
  new_image.save(file + '.png')


if __name__ == '__main__':
  if len(sys.argv) < 4:
    print('./txt2img font size text file (optional)')
    exit(1)

  file = 'out'

  if len(sys.argv) == 5:
    font, size, text, file = sys.argv[1:]
  else:
    font, size, text = sys.argv[1:]

  main(font, size, text, file)
