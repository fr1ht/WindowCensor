#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

from fnc import show_image


class DetectIP:
  """
  """
  def __init__(self, image, template):
    self.image = image
    self.template = template


  def matching(self):
    img = self.image
    imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
    contours , _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)


        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5

        # if len(approx) == 3:
        #     cv2.putText( img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0) )

        if len(approx) > 4 :
            x, y , w, h = cv2.boundingRect(approx)
            aspectRatio = float(w)/h
            cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)

            # print(aspectRatio)

            # if aspectRatio >= 0.95 and aspectRatio < 1.05:
            #     cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.1l, (0, 0, 0))

            # else:
            #     cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

        # elif len(approx) == 5 :
        #     cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        # elif len(approx) == 10 :
        #     cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        # else:
        #     cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    show_image(img)

  def main(self):
    self.matching()
    exit()
    w, h = template.shape
    for ridx in range(w):
      print(self.template[ridx])
      continue

      for cidx, col in enumerate(range(h)):
        r, g, b = self.template[ridx][cidx]
        print(r, g, b)
        exit()
    show_image(self.template)


if __name__ == '__main__':
  filename = '../ipExample/pics/res.png'
  image = cv2.imread(filename)

  template_filename = 'rip.png'
  template = cv2.imread(template_filename, 0)

  dip = DetectIP(image, template)
  dip.main()
