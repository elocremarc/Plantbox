#!/bin/bash
python3 rm.py
cd /home/pi/HDD && gphoto2 --capture-image-and-download --filename capture%n.%C
