import Motor
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


motor = Motor.Motor()
motor.enable()
motor.rotate(-100, -100)
time.sleep(3)
motor.stop()
motor.disable()
