#!/usr/bin/python3

'''This Python Program is based on Gphoto2 which controls many types of camera models
via USB. Gphoto2 runs via the command line, it was adapted to work with python here.
this program also triggers a 2 channel relay in order to control both studio lighting as well as a grow light 
in order to timelapse the growth of a plant. The grow light turns  off during
the photo while the studio light is turned on. The grow light also uses the
datetime function to see if it is daytime. The plant needs to sleep!'''


import time
import RPi.GPIO as GPIO
from time import sleep
import datetime
import sh
from sh import gphoto2 as gp
import signal, os, subprocess


growpin = 20 #GPIO Pin 20
studiopin = 21 #GPIO Pin 21
counter = 1
interval = 225 # 450 #Set the Timelapse Interval
dir = "/home/pi/HDD/"
picID = "Test123" #Project Name
save_location = dir + picID +"/"


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(growpin, GPIO.OUT)
GPIO.setup(studiopin, GPIO.OUT)


shot_date = datetime.datetime.now().strftime("%Y-%m-%d")
shot_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Mount Drive
def Mount():
	os.system("mount " + dir )


#Create Save Folder fucntion
def createSaveFolder():
    try:
        os.makedirs(save_location)
    except:
        print("Directory Already Exists")
        os.chdir(save_location)


# Remove Residual Capture1 & Capture2 from folder that coud hang the Gphoto2 bash script
def cleanFolder ():
	os.chdir(save_location)
	if os.path.exists("capture1.jpg"):
		os.remove("capture1.jpg")
	if os.path.exists("capture2.cr2"):
		os.remove("capture2.cr2")

# Move to working directory, Using gphoto2, Capture Image, Download, Rename jpg file to Capture 1 & the raw file to Capture 2	
def gphotoCapture ():
	os.system("gphoto2 --capture-image-and-download --filename " + save_location + "capture%n.%C")

# Rename Files with Timestamp and Project name
def renameFiles(ID):
    for filename in os.listdir("."):
        if len(filename) < 13:
            if filename.endswith(".jpg"):
                os.rename(filename, (ID + " " + str(counter) + ".JPG"))
                print("Renamed the JPG")
            if filename.endswith(".cr2"):
                os.rename(filename, (ID + " " + str(counter) + ".CR2"))
                print("Renamed the cr2")

# Combine functions in order of operation to take a picture onto the pi
def CaptureImage ():
	Mount()
	createSaveFolder()
	cleanFolder()
	gphotoCapture()
	renameFiles(picID)

#This function determines if the sun is up based on the range in the if statement
def growLight():

    now = datetime.datetime.now()
    str(now)
    intervalmins = interval / 60
    str(intervalmins)
    print("Interval:",intervalmins, " Minutes" )

    if now.hour > 7 and now.hour < 17:

        
        GPIO.setup(growpin, GPIO.OUT)
        GPIO.output(growpin, GPIO.LOW)
        print("Grow on")
    else:
        
        GPIO.setup(growpin, GPIO.OUT)
        GPIO.output(growpin, GPIO.HIGH)
        print("Grow off")

while True:
        
        # Time Stamp
        shot_date = datetime.datetime.now().strftime("%Y-%m-%d")
        shot_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Header
        print ("/" * 16 , " Time Lapse " ,picID ,counter,"||||||",shot_time, "/" *16 )
        #Setup GPIO set growpin and studiopin as outputs
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(growpin, GPIO.OUT)
        GPIO.setup(studiopin, GPIO.OUT)
        
        # Turn Grow Light Off Turn on Studio to prepare for the picture to be taken
        GPIO.output(growpin, GPIO.HIGH)
        GPIO.output(studiopin, GPIO.LOW)
        
        print("/"*8, "Image Capture", "/"*8)
        # Take Picture
        CaptureImage()
        

        # Turn off Studio Lights after photo is taken
        GPIO.output(studiopin, GPIO.HIGH)
        growLight()
        sleep(interval)
        
        #Clean up GPIO
        GPIO.cleanup()
        counter += 1
