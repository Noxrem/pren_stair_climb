import time
import RPi.GPIO as GPIO
import logging


class UltrasonicModule:
    def __init__(self, name, echo_gpio, trigger_gpio):
        logging.info("create new ultrasonic module")
        self.name = name
        self.echo_gpio = echo_gpio
        self.trigger_gpio = trigger_gpio
        self.offset = 0.0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_gpio, GPIO.OUT)
        GPIO.setup(self.echo_gpio, GPIO.IN)
        self.amount_of_multiple_measurements = 5

    def get_distance(self):
        logging.debug("ultrasonic module get distance")
        # set Trigger to HIGH
        GPIO.output(self.trigger_gpio, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.trigger_gpio, False)

        start_time = time.time()
        stop_time = time.time()

        # save start_time
        while GPIO.input(self.echo_gpio) == 0:
            start_time = time.time()

        # save time of arrival
        while GPIO.input(self.echo_gpio) == 1:
            stop_time = time.time()

        # time difference between start and arrival
        time_elapsed = stop_time - start_time

        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance_in_cm = (time_elapsed * 34300) / 2

        return distance_in_cm

    def get_distance_multiple_in_cm(self):
        logging.debug("get distance multiple in cm")
        distances = []
        counter = 0
        sum_distances = 0
        for i in range(self.amount_of_multiple_measurements):
            distance = self.get_distance()
            distances.insert(counter, distance)
            sum_distances += distance
            counter += 1
        distance = sum_distances / self.amount_of_multiple_measurements
        return distance
