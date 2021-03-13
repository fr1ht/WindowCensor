#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
from PIL import Image, ImageFont, ImageDraw
import numpy as np
from collections import Counter


def show_image(image):
  plt.imshow(image)
  plt.show()



def draw_text_to_image(image, font_size):
  # clean_page = np.ones(image.size)
  draw = ImageDraw.Draw(image)
  x, y = (0, 0)
  font = ImageFont.truetype('FiraCode-Regular.ttf', size=font_size)
  message = "Happy Birthday!"
  color = 'rgb(255, 255, 255)'
  draw.text((x, y), message, fill=color, font=font)
  show_image(image)


def get_pixel_height(image):
  hes = []
  medians = []
  mx = 0

  (width, height) = image.size

  zeros = np.zeros(image.size)

  for w in range(width):
    for h in range(height):
      rgb = sum(image.getpixel((w, h)))
      zeros[w, h] = 0 if rgb > 300 else 1

    prev = 0
    max_h = 0

    for h in range(height):
      h = zeros[w, h]
      if not prev and h:
        prev = h
        max_h += 1
      elif h != 0 and prev:
        max_h += 1
      else:
        if max_h and max_h not in hes:
          hes.append(max_h)
        prev = 0
        max_h = 0

    hes.append(max_h)

  font_size = Counter(hes).most_common(1)[0][0]
  draw_text_to_image(image, font_size)

def main(image):
  # show_image(image)
  get_pixel_height(image)


"""
"""



if __name__ == '__main__':
  hidden_ip = 'HideMe.png'
  image = Image.open(hidden_ip)
  main(image)
