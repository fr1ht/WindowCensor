#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple


MONITOR_RES = namedtuple(
  'MONITOR_RES', ['w', 'h']
)


def get_monitor_resolution() -> str:
  import subprocess
  from re import findall

  # XXX: "xrandr | grep '*'"
  monitor_resolutions = subprocess.Popen(["xrandr"], stdout=subprocess.PIPE)
  # XXX: b'   1920x1080     60.01*+  59.93  \n'
  monitor_resolution = subprocess.check_output(
    ("grep", "*"), stdin=monitor_resolutions.stdout
  ).decode()
  monitor_resolutions.wait()

  delimiter = 'x'

  return MONITOR_RES(
    *(
      map(
        lambda x: int(x),
        (findall(f"\d+{delimiter}\d+", monitor_resolution)[0]).split(delimiter)
      )
    )
  )


if __name__ == '__main__':
  print(get_monitor_resolution())
