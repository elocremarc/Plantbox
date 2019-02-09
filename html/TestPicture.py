
'''This Python program will capture an image with gphoto2 and rename it to test. It will then delete the previous one on the directory This is usefull for taking a test photo to check exposure and compostion when setting the exposure with gphoto2'''

import time
import os
import shutil

Directory = "/var/www/html"

# Remove Residual Capture1 & Capture2 from folder that coud hang the Gphoto2 bash script
def cleanFolder ():
        os.chdir(Directory)
        if os.path.exists("test1.jpg"):
                os.remove("test1.jpg")
        if os.path.exists("test2.cr2"):
                os.remove("test2.cr2")

# Move to working directory, Using gphoto2, Capture Image, Download, Rename jpg file to Capture 1 & the raw file to Capture 2	
def gphotoCapture ():
        os.system("cd /var/www/html && gphoto2 --capture-image-and-download --filename test%n.%C")
        


# Combine functions in order of operation to take a picture onto the pi
def CaptureImage ():
        cleanFolder()
        time.sleep(2)
        gphotoCapture()
        time.sleep(3)
    



CaptureImage()

