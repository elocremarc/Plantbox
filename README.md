# Plantbox
## Plant Box Project:
Purpose: This project is based on the Raspberry Pi. Its goal is to film the timescales of life. This is done through the timelapsing of plants. The project is intended to create a "Plant Box" an issolated place where a plant will grow for the sole purpose of being photographed. This "Plant Box" will have a controller to manage studio lights as well as grow lights to sustain the growth. The controller will also trigger and download images from any camera to a HDD. The goal of this is to fully automate the process and elimiate any human interaction during the entire growth of the plant cycle. Plants, especially flowers need sleep therefore it is important that a plant receive light only half the day. Therefore the grow light must be controlled to be on only half the day. These grow lights typically are purple and have nasty coloring for photography. Therefore its important that this light also be turned off whilst the photo is being taken. To light up the scene a second light is needed while the grow light is off.

# Guide
## Gphoto2
Gphoto2 is a Command Line interface for controlling many differnt camera models through a USB connection. This project was developed on the 60D so be sure to look at the Gphoto2 documentaion to see if your camera is supported.
http://gphoto.org/proj/libgphoto2/support.php 

Install Gphoto2 with the following commands.

Update the Pi:
```
$ sudo apt-get install update
```
Install Gphoto2:
```
$ sudo apt-get install Gphoto2
```

Once Gphoto2 is installed we need to make sure the files are stored to the memory card of the camera. We do this by typing in the following commands. 
```
$ gphoto2 --set-config capturetarget=1
```
To confirm run the following command:
```
$ gphoto2 --get-config capturetarget
```
Make sure the Capture Target is:
```
 Current:Memory Card
```
## Python Program
This Python Program uses GPIO and Gphoto2 which was adapted to work with python in this program. 
This adaptaion was was created by the instructions in this YouTube video. I would recomend watching that video because this is what this program is based on. He explains how to use Gphoto2 extensivly as well.
https://www.youtube.com/watch?v=1eAYxnSU2aw

He also explains that you will also need some dependecies along with Gphoto2 for the python program to work. Install them with the following comands:
```
$ sudo apt-get install python3-pip
```
```
$ sudo pip3 install sh
```
Other than the fucntions achived in the video this program also triggers 
a 2 channel relay with GPIO pins in order to control both studio lighting as well as a grow light. 
The grow light turns off during the photo while the studio light is turned on. The grow light also will only shine during the day. 

## Wiring
Along with connecting the camera to the USB on the Pi a 2 channel relay must also be connected to 2 GPIO pins on the Pi. These control another higher voltage circuit than the raspbery Pi's 5volt. You can use this to control 12 Volt LED strips for both studio lights and grow lights. These are symbolized as LED's on the following diagram.

![alt text](https://github.com/elocremarc/Plantbox/blob/master/2%20Channel%20Relay%20Raspberry%20Pi.jpg)
Pins 2 & 3 on the Pi are the pins that we will used to control the relay. They connect to the relay board along with the 5Volt VCC and the Ground of the Rasperry Pi. This can be used to control Mains power or a safer option if your not electrically confident is using 12Volt LEDs they have LED strips for both Daylight and GrowLight

## File Storage Location
Currently the python program is saving files to the desktop of the raspbery pi in a folder named timelapse.
create this folder with the following commands:
```
$ sudo mkdir /home/pi/Desktop/timelapse
```
 change this location by changing the save path in the save location function in the python program
```
save_location = "/home/pi/Desktop/timelapse" + folder_name
```
You can point the save location function to a HDD but you must first have the HDD mounted to a directory.
Follow these instructions to mount a HDD to a directory: 
https://www.raspberrypi.org/documentation/configuration/external-storage.md
## Running The Program
```
$ python3 PlantLapse.py
```
This will run as long as terminal is open. You can make the program run after terminal is closed with this command:
```
$ nohup python3 PlantLapse.py &
```
Note: you must close the process down manually to stop the script. Find the python3 process with the following command:
```
$ ps -A | grep python3
```
You will get a number back followed by other characters. This is the command we must kill. Kill it with the kill command:
```
$ kill XXXX
```
