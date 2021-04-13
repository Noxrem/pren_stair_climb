import Motor
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')



motor = Motor.Motor()
motor.motor_help()
motor.drive_help()
