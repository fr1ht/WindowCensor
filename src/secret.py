#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Xlib
from Xlib import display, X
from PIL import Image, ImageFont, ImageDraw
import cv2
import numpy as np

from matplotlib import pyplot as plt


import re


import pytesseract


def show_image(image):
  plt.imshow(image)
  plt.show()


class Window:

  def txt2ip(self, snapshot_text):
    for ip in re.findall('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', snapshot_text):
      yield ip

  def img2txt(self, snapshot):
    gray = cv2.cvtColor(np.array(snapshot), cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    text = pytesseract.image_to_string(snapshot)
    return text

  def ip2img(self, ip):

    def create_image(size):
      return Image.new('RGB', size, 'white')

    def get_size(size, ip):
      width, height = size.split('x')

      height = int(height)

      if not width:
        width = len(ip) * (7)

      return int(width), height

    x, y = (0, 0)
    size = 'x11'
    size = get_size(size, ip)
    new_image = create_image(size)
    font = 'FiraCode-Medium.ttf'

    font = ImageFont.truetype(font, size=size[1])
    draw = ImageDraw.Draw(new_image)

    color = 'black'

    draw.text((x, y), ip, fill=color, font=font)
    return new_image

  def ip_coordinates(self, snapshot, ip_image):
    img_rgb = snapshot
    img_gray = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_BGR2GRAY)
    ip_image.save('temp_ip.png')
    template = cv2.imread('temp_ip.png', 0)

    height, width = template.shape[:]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_SQDIFF)
    # plt.imshow(res, cmap='gray')

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = min_loc  #Change to max_loc for all except for TM_SQDIFF
    bottom_right = (top_left[0] + width, top_left[1] + height)
    # cv2.rectangle(img_rgb, top_left, bottom_right, (255, 0, 0), 2)
    return (top_left, bottom_right)

  def hide_ip(self, root, dsp, gc, top_left, right_bottom, ip):
    # print(('1'*len(ip)).encode())
    # print(top_left, right_bottom)
    root.draw_text(gc, top_left[1], right_bottom[1], ('k'*len(ip)).encode())
    dsp.flush()

  def main(self):
    """Take a screenshot
    """
    # w, h = self.get_current_resolution()

    # XXX, FIXME: dev screen resolution is used!

    w, h = (1920, 1080)
    dsp = display.Display()
    screen = dsp.screen()
    root = dsp.screen().root
    gc = root.create_gc(foreground = screen.black_pixel, background = screen.black_pixel)

    while True:
      raw = root.get_image(0, 0, w, h, X.ZPixmap, 0xffffffff)
      snapshot = Image.frombytes("RGB", (w, h), raw.data, "raw", "BGRX")
      snapshot_text = self.img2txt(snapshot)

      # snapshot_text = ' flsflseflsefk 94.130.179.24 3wrwwl elkjf ijpoiarpr9'
      for ip in self.txt2ip(snapshot_text):
        ip_image = self.ip2img(ip)
        top_left, right_bottom = self.ip_coordinates(snapshot, ip_image)
        self.hide_ip(root, dsp, gc, top_left, right_bottom, ip)


if __name__ == '__main__':
  window = Window()
  window.main()
