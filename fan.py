# Used with BS170 N-channel mosfet with following connections
# GND - BS170 Source
# 5V - Fan VCC
# Pin 19 - BS170 Gate
# Fan GND - BS170 Drain

import RPi.GPIO as GPIO
import time
import os
import argparse

parser = argparse.ArgumentParser()

# add arguments to the parser
parser.add_argument("pin_number")
parser.add_argument("min_temp")
parser.add_argument("max_temp")

# parse the arguments
args = parser.parse_args()

fan_pin = int(args.pin_number)
duty = 0
run_delay = 1
min_temp = int(args.min_temp)
max_temp = int(args.max_temp)

status = "Pin: {0}, Min. temp: {1}, Max. temp {2}".format(str(fan_pin), str(min_temp), str(max_temp))
print(status)

GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_pin, GPIO.OUT)

p = GPIO.PWM(fan_pin, 100)

def get_temp():
    cmd = "vcgencmd measure_temp"
    temp_val = str(os.popen(cmd).read())
    temp_val = float(temp_val.replace("temp=", "").replace("'C",""))
    return temp_val

def mapval(x, in_min, in_max, out_min, out_max):
    value = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return value

try:
    p.start(duty)
    while True:
        temp = int(get_temp())
        if temp < min_temp:
            fan_rpm = 0
        else:
            fan_rpm = int(mapval(temp, min_temp, max_temp, 60, 100))
        
        p.ChangeDutyCycle(fan_rpm)
        
        time.sleep(run_delay)

except KeyboardInterrupt: 
    p.ChangeDutyCycle(0)
    p.stop()
    GPIO.cleanup() 

