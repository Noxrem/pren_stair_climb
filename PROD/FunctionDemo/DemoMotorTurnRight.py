import Motor
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


motor = Motor.Motor()
motor.enable()
motor.rotate(-30, 30)
time.sleep(5)
motor.stop()
motor.disable()
