#!/usr/bin/python
import os

# Remove Residual Capture1 & Capture2 from folder that coud hang the Gphoto2 bash script
if os.path.exists("capture1.jpg"):
    os.remove("capture1.jpg")
if os.path.exists("capture2.cr2"):
    os.remove("capture2.cr2")
