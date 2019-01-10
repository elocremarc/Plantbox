#!/usr/bin/python

import datetime
import os



#This is where you specify the name of the project for filenaming
picID = "PlantShots"

#Lets get timestamped!
def timeStamp ():
	shot_date = datetime.datetime.now().strftime("%Y-%m-%d")
	shot_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Remove Residual Capture1 & Capture2 from folder that coud hang the Gphoto2 bash script
def cleanFolder ():
	if os.path.exists("capture1.jpg"):
		os.remove("capture1.jpg")
	if os.path.exists("capture2.cr2"):
		os.remove("capture2.cr2")

# Move to working directory, Using gphoto2, Capture Image, Download, Rename jpg file to Capture 1 & the raw file to Capture 2	
def gphotoCapture ():
	os.system("cd /home/pi/HDD && gphoto2 --capture-image-and-download --filename capture%n.%C")

# Rename Files with Timestamp and Project name
def renameFiles(ID):
    for filename in os.listdir("."):
        if len(filename) < 13:
            if filename.endswith(".jpg"):
                os.rename(filename, (shot_time + ID + ".JPG"))
                print("Renamed the JPG")
            if filename.endswith(".cr2"):
                os.rename(filename, (shot_time + ID + ".CR2"))
                print("Renamed the cr2")

# Run all functions in order of operation to take a picture onto the pi 				
def CaptureImage ():
	cleanFolder()	
	timeStamp()
	gphotoCapture()	
	renameFiles(picID)

