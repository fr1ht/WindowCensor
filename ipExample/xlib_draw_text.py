#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Xlib
from Xlib import display, X   # X is also needed

display = Xlib.display.Display()
screen = display.screen()
root = screen.root

#print(root.get_attributes())
root.change_attributes(event_mask=X.ExposureMask)  # "adds" this event mask
#print(root.get_attributes())  # see the difference

gc = root.create_gc(foreground = screen.white_pixel, background = screen.black_pixel)


def draw_it():
  root.draw_text(gc, 100, 100, b"Hello, world!")
  display.flush()


draw_it()


while 1:
  if display.pending_events() != 0:  # check to safely apply next_event
    event = display.next_event()
    if event.type == X.Expose and event.count == 0:
      draw_it()
