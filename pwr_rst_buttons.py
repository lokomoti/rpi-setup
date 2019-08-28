#!/bin/python 
# Simple script for shutting down the raspberry Pi at the press of a button. 
# by Inderpreet Singh 
import RPi.GPIO as GPIO  
import time  
import os

pwr_pin = 36
rst_pin = 40

# Setup the Pin with Internal pullups enabled and PIN in reading mode. 
GPIO.setmode(GPIO.BOARD)

GPIO.setup(pwr_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)  
GPIO.setup(rst_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Our function on what to do when the button is pressed 
def Shutdown(channel):
    print("shutdown")
   #os.system("sudo shutdown -h now")  
def Restart(channel):
    print("reboot")
    os.system("sudo shutdown -r now")
   
# Add our function to execute when the button pressed event happens 
GPIO.add_event_detect(pwr_pin, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)  
GPIO.add_event_detect(rst_pin, GPIO.FALLING, callback = Restart, bouncetime = 2000) 
# Now wait! 
while 1:  
   time.sleep(1) 