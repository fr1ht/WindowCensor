#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import pytesseract
from PIL import Image


def main():
    # Get File Name from Command Line
    # path = input("Enter the file path : ").strip()
    path = 'fu.png'

    # Load the required image
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    preprocess = False
    # temp = input(
    #     "Do you want to pre-process the image ?\nThreshold : 1\nGrey : 2\nNone : 0\nEnter your choice : ").strip()

    temp = "1"
    # If user enters 1, Process Threshold. Else if user enters 2, Process Median Blur. Else, do nothing
    if temp == "1":
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif temp == "2":
        gray = cv2.medianBlur(gray, 3)

    # Store grayscale image as a temporary file to apply OCR
    filename = "{}.png".format("temp")
    cv2.imwrite(filename, gray)

    # Load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
    text = pytesseract.image_to_string(Image.open(filename))

    print("OCR Text is " + text)


try:
    main()
except Exception as e:
    print(e.args)
    print(e.__cause__)

