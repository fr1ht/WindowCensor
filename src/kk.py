#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from window import Window
from fnc import show_image

window = Window()

image = window.get_image()
show_image(image)


window.censor()
