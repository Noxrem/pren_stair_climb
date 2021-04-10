# Copyright Nathanael Birrer HSLU

# Description
# Accelerator module control

# Useful links
# Shop:
# Code example 1: https://tutorials-raspberrypi.com/measuring-rotation-and-acceleration-raspberry-pi/
# Code example 2: https://learn.adafruit.com/mpu6050-6-dof-accelerometer-and-gyro/python-and-circuitpython
# Remote debug: https://www.youtube.com/watch?v=oikrc1lEMXg&ab_channel=szparacha
# Python version: https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux

#Prerequisites
#sudo pip3 install adafruit-circuitpython-mpu6050

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import adafruit_mpu6050

GPIO_SDA  = 2
GPIO_SCL = 3

i2c = busio.I2C(GPIO_SCL, GPIO_SDA)
AcceleratorModule = adafruit_mpu6050.MPU6050(i2c)

def get_acceleration_x():
    x_axes = 0
    return AcceleratorModule.acceleration.__getitem__(x_axes);

def get_acceleration_y():
    y_axes = 1
    return AcceleratorModule.acceleration.__getitem__(y_axes);

def get_acceleration_z():
    z_axes = 2
    return AcceleratorModule.acceleration.__getitem__(z_axes);

def get_temperature_in_celsius():
    return AcceleratorModule.temperature