# Plantbox
## Plant Box Project:
The goal of this project is to is to film the timescales of life. This is done through the timelapsing of plants using the Raspberry Pi. The project is intended to create a "Plant Box" an issolated place where a plant will grow for the sole purpose of being photographed. This "Plant Box" will have a controller to manage studio lights as well as grow lights to sustain the growth. The controller will also trigger and download images from any camera to an external HDD. The goal of this is to fully automate the process and eliminate any human interaction during the entire growth of the plant cycle.

# Items Needed

You will need the following items in order to create your own plant box.
- 1 x Raspberry Pi (any model)
- 1 x Micro SD with Rasbian Installed
- 1 x Keyboard/Mouse & Monitor (only needed to connect to the network)
- 1 x Raspberry Pi Power supply
- 1 x 2 Channel Relay Module
- 4 x Jumper cables to connect the relay to the Pi
- 1 x 12 Volt Daylight LED strip
- 1 x 12 Volt Growlight LED strip
- 1 x 12 Volt LED power Supply
- 1 x "Plant Box" a quite dark place where a plant can grow undisturbed. 

# Guide
## Installing This App
### Fresh Rasberry Pi 
You need to have a raspberry Pi with the latest version of Rasbian/Noobs up and running before you begin this guide. If you haven't done so already follow the offical guide to get up and running. 
https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up
### SSH into Your Pi.
If you have your Raspberry Pi up and running with a keyboard and mouse and monitor your can ditch these and finish the rest of the project using SSH on your personal computer. Make sure it is connected to your local wifi network first. Open terminal so you can find the IP address of your raspberry pi using the following command.
```
$ ifconfig
```
Once you find your ip adress you can open up Terminal in Mac/Linux and Command Prompt for Windows and start a SSH session typing the following command. 
```
$ SSH pi@ip.address.of.your.pi
```
You will then answer "yes" to start a new SSH session with your remote Raspberry Pi. It will ask you to enter a password if you haven't changed the password it should be "raspberry"
```
Password:raspberry
```
It is highly recommended that you change the password to the Pi immediately. Change the password inside of raspi-config.
```
$ sudo rasp-config
```
You might need to reconnect to your SSH session after you change your password. Once you are connected to your Raspberry Pi with a SSH connection you are ready to install this app.

Make sure your have Git installed.
```
$ sudo apt-get install git
```
Open Terminal and cd into the directory where you want to install this repository. 
```
$ cd~/Directory/Where/You/Want/This/Repository
```
Install Plantbox repository:
```
$ git clone https://github.com/elocremarc/Plantbox
```
You will need some addional programs and python packages in order for the python program to function properly.

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
Make sure the capture target is:
```
 Current:Memory Card
```
## Python Program
This Python Program uses GPIO and Gphoto2 which was adapted to work with python in this program. 
This adaptaion was was created by the instructions in this YouTube video. I would recomend watching that video because is what the program is based on. He explains how to use Gphoto2 extensivly as well.
https://www.youtube.com/watch?v=1eAYxnSU2aw

You will also need some dependecies along with Gphoto2 for the python program to work. Install them with the following comands:
```
$ sudo apt-get install python3-pip
```
```
$ sudo pip3 install sh
```
Other than the fucntions achived in the video this program also triggers a 2 channel relay to control both studio light and a grow light. The grow light turns off during the image cpature while the studio light is turned on. The grow light also will only shine during the day. 

## Wiring
Along with connecting the camera to the USB on the Pi a 2 channel relay must also be connected to 2 GPIO pins on the Pi. These control a  higher voltage circuit for instance a 12 volt LED strip. 12 volt LED strips work great because you can get them for both Daylight and GrowLight. These "Lights" are symbolized as LED's on the following schematic. Output side of the relay is where you would need to the appropriate 12 volt power supply to power your LED strip setup. 

![alt text](https://github.com/elocremarc/Plantbox/blob/master/2%20Channel%20Relay%20Raspberry%20Pi.jpg)

Pins 2 & 3 on the Pi are the pins that we will used to control the relay. They connect to the relay board along with the 5 Volt VCC pin and the Ground Pin of the Rasperry Pi. This can be used to control Mains power or a safer option is using 12Volt LEDs

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
cd into the path where the python program is located:
```
$ cd /Path/to/file/PlantLapse.py
```
Run this program using python3:
```
$ python3 PlantLapse.py
```
This will run so long as as terminal is open. It will stop once terminal is closed. You can make the program run in its own serpate independent shell with this command:

```
$ nohup python3 PlantLapse.py &
```
Note: you must close the process down manually to stop the script. Find the python3 process with the following command:
```
$ ps -A | grep python3
```
You will get a number back followed by other characters:
```
$ XXXX pts/0 00:00:03 python3 
```
Use this number with the kill command to stop the PlantLapse.py:
```
$ kill XXXX
```
