#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt


def get_template(img):
  img = cv2.imread(img)
  return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def matches(img1, img2):
  img1 = get_template(img1)
  img2 = get_template(img2)

  # methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
  methods = [cv2.TM_CCOEFF_NORMED]

  for method in methods:
    # match = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
    # match = cv2.matchTemplate(img1, img2, method)

    img = img1
    template = img2
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(str(method))

    plt.show()



def mario(img1, img2):
  img_gray = get_template(img1)
  img_rgb = img_gray.copy()
  # template = get_template(img2)
  w, h = template.shape[::-1]

  methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

  step = 1
  res = cv2.matchTemplate(img_gray,template, methods[step])
  threshold = 0.8
  loc = np.where( res >= threshold)
  for pt in zip(*loc[::-1]):
      cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255,0,0), 2)

  cv2.imwrite('res.png',img_rgb)







    # threshold = 0.8
    # position = np.where(match >= threshold)
    #
    # print(position)
    # # if position[0].size:
    # #   return 'HY'
    #

if __name__ == '__main__':
  img1 = 'fuf.png'
  img2 = 'out.png'

  matches(img1, img2)
  # mario(img1, img2)
