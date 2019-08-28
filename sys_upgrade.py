#!/bin/python 

from time import sleep as delay
import os

os.system("sudo apt-get update")
print("update done!")
print("\n")

delay(10)

print("upgrade start!")
os.system("sudo apt-get dist-upgrade -y")
print("upgrade done!")

