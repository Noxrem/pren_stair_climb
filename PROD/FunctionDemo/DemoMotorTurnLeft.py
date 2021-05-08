import Motor
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


motor = Motor.Motor()
motor.enable()
motor.rotate(50, -50)
time.sleep(5.9)
motor.stop()
motor.disable()
