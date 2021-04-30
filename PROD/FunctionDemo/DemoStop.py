import Motor
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


motor = Motor.Motor()
motor.enable()
motor.stop()
motor.disable()
