# Code example: https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/
# Remote debug: https://www.youtube.com/watch?v=oikrc1lEMXg&ab_channel=szparacha
# Python version: https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux

import time
from UltrasonicModule import UltrasonicModule
import numpy
import logging


class UltrasonicModuleControl:

    NUMBER_MEASUREMENTS = 20

    # Define sensor module 1
    sensor_front = None
    GPIO_TRIGGER_1 = 18
    GPIO_ECHO_1 = 17

    # Define sensor module 2
    sensor_side = None
    GPIO_TRIGGER_2 = 17
    GPIO_ECHO_2 = 22

    # Define sensor list
    sensor_list = None

    def __init__(self):
        logging.info("create new ultrasonic module control")
        self.sensor_front = UltrasonicModule("sensor_front", self.GPIO_ECHO_1, self.GPIO_TRIGGER_1)
        self.sensor_side = UltrasonicModule("sensor_side", self.GPIO_ECHO_2, self.GPIO_TRIGGER_2)
        self.sensor_list = [self.sensor_front, self.sensor_side]

    def get_distance_in_cm(self):
        nr_sensor = 0
        return self.get_distance_mean(self.sensor_list.__getitem__(nr_sensor), self.NUMBER_MEASUREMENTS)

    def get_distance_mean(self, sensor, numbers_measurements):
        values = numpy.empty([numbers_measurements])
        for count in range(numbers_measurements):
            values[count-1] = sensor.get_distance()
            # Sleep as influence on accuracy
            time.sleep(0.05)
        return values.mean() - sensor.offset

    def calibrate_sensor(self, sensor, distance_sensor_to_object):
        calibration_ongoing = True
        while calibration_ongoing:
            distance = self.get_distance_mean(sensor, self.NUMBER_MEASUREMENTS)
            sensor.offset = distance - distance_sensor_to_object
            distance = self.get_distance_mean(sensor, self.NUMBER_MEASUREMENTS)
            if distance - distance_sensor_to_object < 0.05:
                calibration_ongoing = False
                logging.info(f"Calibration of sensor {sensor.name} successful: Offset = %.2f cm" % sensor.offset)
            else:
                sensor.offset = 0

    def calibrate_sensors(self, distance_sensor_to_object):
        for sensor in self.sensor_list:
            self.calibrate_sensor(sensor, distance_sensor_to_object)
