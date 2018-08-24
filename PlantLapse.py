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
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(growpin, GPIO.OUT)
GPIO.setup(studiopin, GPIO.OUT)
daytime = 1

# Kill gphoto2 process that
# starts whenever we connect the
# camera

def killgphoto2Process():
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()
	
    # Search for the line that has the process
    # we want to kill
    for line in out.splitlines():
        if b'gvfsd-gphoto2' in line:
            # Kill the process!
            pid = int(line.split(None,1)[0])
            os.kill(pid, signal.SIGKILL)

shot_date = datetime.datetime.now().strftime("%Y-%m-%d")
shot_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#This is where you specify the name of the timelapse for filenaming
picID = "PlantShots"

# This will clear the files off the SD card
#	Note: "/store_00020001/DCIM/100CANON" might be difffernt based on your camera'''
clearCommand = ["--folder", "/store_00020001/DCIM/100CANON",\
                "-R", "--delete-all-files"]


#Trigger Command
triggerCommand = ["--trigger-capture"]

#Download Command
downloadCommand = ["--get-all-files"]

folder_name = shot_date + picID


#        	This is where you want to specify where the timelapse photos will be saved.
#		If you want to save to an external HDD make sure you mount it to a directory
#		More info about mounting a HDD can be found here.
#		https://www.raspberrypi.org/documentation/configuration/external-storage.md
		
save_location = "/home/pi/Desktop/timelapse" + folder_name

#Create Save Folder fucntion
def createSaveFolder():
    try:
        os.makedirs(save_location)
    except:
        print("Failed to create the new directory.")
        os.chdir(save_location)

#Capture Image fucntion 
def captureImages():
    gp(triggerCommand)
    sleep(3)
    gp(downloadCommand)
    gp(clearCommand)

#Rename Function function 
def renameFiles(ID):
    for filename in os.listdir("."):
        if len(filename) < 13:
            if filename.endswith(".JPG"):
                os.rename(filename, (shot_time + ID + ".JPG"))
                print("Renamed the JPG")
            if filename.endswith(".CR2"):
                os.rename(filename, (shot_time + ID + ".CR2"))
                print("Renamed the CR2")

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
		
killgphoto2Process()
gp(clearCommand)

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

	# Gphoto2 Camera Operations
    createSaveFolder()
    captureImages()
    renameFiles(picID)

	# Turn off Studio Lights after photo is taken
    GPIO.output(studiopin, GPIO.HIGH)

	# Check to See if the sun is up
    suncheck()

#	If the sun is "up" our boolean "daytime" should equal true.
#	Therefore we turn on the grow light and print grow light on.
#	If it is night we dont want the grow light on so we
#	turn off the grow light and print grow off 
	
    if daytime:
        GPIO.setup(growpin, GPIO.OUT)
        GPIO.output(growpin, GPIO.LOW)
        print("Grow on")
    else:
        GPIO.setup(growpin, GPIO.OUT)
        GPIO.output(growpin, GPIO.HIGH)
        print("Grow off")

	#Set the Timelapse Interval

    interval = 52
    sleep(interval)

	#Clean up GPIO
    GPIO.cleanup()
