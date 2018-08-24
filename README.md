# Plantbox
## Plant Box Project:
This Project is to film the timescales of life. This is done through timelapsing of plants. Plants, especially flowers need sleep therefore it is important that a plant gets light only half the day. This means that a grow light must be controlled to turn on only half the day. These grow lights typically are purple and have gross coloring for photography. Therefore its important that this light be turned off whilst the photo is being taken. To light up the scene a second light is needed while the grow light is off.

## Gphoto2
Gphoto2 is a Command Line interface for controlling many differnt camera models including most of Canons through a USB connection. This project was developed on the 60D so be sure to look at the Gphoto2 documentaion to see if your camera is supported. You might need to changed the file path based on your camera on line 50 in the python program
http://gphoto.org/proj/libgphoto2/support.php 
If you don't have Gphoto2 use the following commands:
```
$ sudo apt-get install update
```
```
$ sudo apt-get install upgrade
```
```
$ sudo apt-get install Gphoto2
```

## Python Program
This Python Program uses GPIO and Gphoto2 which  was adapted to work with python in this program. 
This adaptaion was was created by the instructions in this YouTube video.
https://www.youtube.com/watch?v=1eAYxnSU2aw

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
