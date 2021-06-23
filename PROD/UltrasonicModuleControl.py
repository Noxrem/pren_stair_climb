# Code example: https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/
# Remote debug: https://www.youtube.com/watch?v=oikrc1lEMXg&ab_channel=szparacha
# Python version: https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux

import time
from UltrasonicModule import UltrasonicModule
import numpy
import logging

class UltrasonicModuleControl:

    NUMBER_MEASUREMENTS = 5

    # Define sensor module 1
    sensor_front = None
    GPIO_TRIGGER_1 = 27
    GPIO_ECHO_1 = 18

    # Define sensor module 2
    sensor_side = None
    GPIO_TRIGGER_2 = 6
    GPIO_ECHO_2 = 5

    # Define sensor list
    sensor_list = None

    def __init__(self):
        logging.info("create new ultrasonic module control")
        self.sensor_front = UltrasonicModule("sensor_front", self.GPIO_ECHO_1, self.GPIO_TRIGGER_1)
        self.sensor_side = UltrasonicModule("sensor_side", self.GPIO_ECHO_2, self.GPIO_TRIGGER_2)
        self.sensor_list = [self.sensor_front, self.sensor_side]

    def get_distance_in_cm(self, number_sensor):
        logging.debug("ultrasonic module control get distance in cm")
        return self.get_distance_median(self.sensor_list.__getitem__(number_sensor), self.NUMBER_MEASUREMENTS)

    def get_distance_median(self, sensor, numbers_measurements):
        logging.debug("ultrasonic module control get distance median")
        values = numpy.empty([numbers_measurements])
        for count in range(numbers_measurements):
            values[count-1] = sensor.get_distance()
            # Sleep as influence on accuracy
            time.sleep(0.05)
        return numpy.median(values) - sensor.offset

    def calibrate_sensor(self, sensor, distance_sensor_to_object):
        logging.debug("ultrasonic module control calibrate sensor")
        calibration_ongoing = True
        while calibration_ongoing:
            distance = self.get_distance_median(sensor, self.NUMBER_MEASUREMENTS)
            sensor.offset = distance - distance_sensor_to_object
            if 0.3 > (distance - distance_sensor_to_object) > -0.3:
                calibration_ongoing = False
                logging.info(f"Calibration of sensor {sensor.name} successful: Offset = %.2f cm" % sensor.offset)
            else:
                logging.warning(f"Calibration of sensor {sensor.name} not successful: Offset = %.2f cm" % sensor.offset)
                sensor.offset = 0.00

    def calibrate_sensors(self, distance_sensor_to_object):
        logging.debug("ultrasonic module control calibrate sensors")
        for sensor in self.sensor_list:
            self.calibrate_sensor(sensor, distance_sensor_to_object)
