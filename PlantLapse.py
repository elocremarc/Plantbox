'''This Python Program is based on Gphoto2 which controls many types of camera models 
via USB. Gphoto2 runs via the command line, it was adapted to work with python here. 
This program was created by following the instructions on this YouTube video.
https://www.youtube.com/watch?v=1eAYxnSU2aw
Other than the fucntions achived in that video this program also triggers 
a 2 channel relay in order to control both studio lighting as well as a grow light 
in order to timelapse the growth of a plant. The grow light turns  off during
the photo while the studio light is turned on. The grow light also uses the 
datetime function to see if it is daytime. The plant needs to sleep!'''


import time
import RPi.GPIO as GPIO
from time import sleep
import datetime
from sh import gphoto2 as gp 
import signal, os, subprocess


growpin = 2
studiopin = 3
daytime = 1 
interval = 25 #Set the Timelapse Interval

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(growpin, GPIO.OUT)
GPIO.setup(studiopin, GPIO.OUT)
 

#This is where you specify the name of the project for filenaming
picID = "PlantShots"

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

# Combine functions in order of operation to take a picture onto the pi  				
def CaptureImage ():
	cleanFolder()	
	gphotoCapture()	
	renameFiles(picID)

#This function determines if the sun is up based on the range in the if statement
def suncheck():
    now = datetime.datetime.now()
    str(now)
    print(now.hour)
    if now.hour > 7 and now.hour < 17:
        daytime = True;
        print("daytime")
    else:
        daytime = False;
        print("nighttime")
		

#	If the sun is "up" our boolean "daytime" should equal true.
#	Therefore we turn on the grow light and print grow light on.
#	If it is night we dont want the grow light on so we
#	turn off the grow light and print grow off 

def growLight():
	
	# Check to See if the sun is up
	suncheck()
	
	if daytime:
		GPIO.setup(growpin, GPIO.OUT)
		GPIO.output(growpin, GPIO.LOW)
		print("Grow on")
	else:
		GPIO.setup(growpin, GPIO.OUT)
		GPIO.output(growpin, GPIO.HIGH)
		print("Grow off")
		
		
while True:

	shot_date = datetime.datetime.now().strftime("%Y-%m-%d")
	shot_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	
	# Setup GPIO set growpin and studiopin as outputs
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(growpin, GPIO.OUT)
	GPIO.setup(studiopin, GPIO.OUT)
	
	# Turn Grow Light Off Turn on Studio to prepare for the picture to be taken
	GPIO.output(growpin, GPIO.HIGH)
	GPIO.output(studiopin, GPIO.LOW)

	# Take Picture
	CaptureImage()

	# Turn off Studio Lights after photo is taken
	GPIO.output(studiopin, GPIO.HIGH)
	growLight()
	sleep(interval)
	#Clean up GPIO
	GPIO.cleanup()