# Copyright Nathanael Birrer HSLU

# Description
# Ultrasonic module control

# Useful links
# Shop:
# Code example: https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/
# Remote debug: https://www.youtube.com/watch?v=oikrc1lEMXg&ab_channel=szparacha
# Python version: https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux
import time

from UltrasonicModule import UltrasonicModule
import numpy

# Measurments
NUMBER_MEASUREMENTS = 20

# Define sensor module 1
GPIO_TRIGGER_1 = 18
GPIO_ECHO_1 = 17
sensor_1 = UltrasonicModule("1", GPIO_ECHO_1, GPIO_TRIGGER_1)

# Define sensor module 2
#GPIO_TRIGGER_2 = 17
#GPIO_ECHO_2 = 22
#sensor_2 = UltrasonicModule("2", GPIO_ECHO_2, GPIO_TRIGGER_2)

# Add sensor modules
sensor_list = [sensor_1]

def get_distance_in_cm():
    # Add list support
    nr = 0
    return get_distance_mean(sensor_list.__getitem__(nr), NUMBER_MEASUREMENTS)

def get_distance_mean(sensor, numbers_measurements):
    values = numpy.empty([numbers_measurements])

    for count in range(numbers_measurements):
        values[count-1] = sensor.get_distance()
        # Sleep as influence on accuracy
        time.sleep(0.05)

    return values.mean() - sensor.offset

def calibrate_sensor(sensor, distance_sensor_to_object):
    calibration_ongoing = True
    while calibration_ongoing:
        distance = get_distance_mean(sensor, NUMBER_MEASUREMENTS)
        sensor.offset = distance - distance_sensor_to_object
        distance = get_distance_mean(sensor, NUMBER_MEASUREMENTS)
        if distance - distance_sensor_to_object < 0.05:
            calibration_ongoing = False
            print(f"Calibration of sensor {sensor.name} successful: Offset = %.2f cm" % sensor.offset)
        else:
            sensor.offset = 0

def calibrate_sensors(distance_sensor_to_object):
    for sensor in sensor_list:
        calibrate_sensor(sensor, distance_sensor_to_object)
