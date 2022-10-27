#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
- VideoProcessing
    - ImageProcessing
        - DigitDetection
            - Logic
"""

if not __debug__:
    from data.input.display import Display
else:
    from data.input.display import Test
from processing.image import Image


def main():
    Test.echo()
