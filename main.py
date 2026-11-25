#!/usr/bin/env python3
"""Write the 25 November 2026 world-news image to /output/entry.png.

The image ("Today's Menu" — the day's news served as a restaurant menu board,
white background, 25 numbered stories led by the Riyadh strike) is stored as
image.png in this repository; this program copies it to the required output.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.png")
DST = "/output/entry.png"

os.makedirs("/output", exist_ok=True)
shutil.copyfile(SRC, DST)
with open(DST, "rb") as f:
    assert f.read(8) == b"\x89PNG\r\n\x1a\n", "output is not a PNG"
print("wrote", DST, os.path.getsize(DST), "bytes")
