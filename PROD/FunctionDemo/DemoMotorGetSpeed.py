import Motor
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

motor = Motor.Motor()
logging.info("**************************Speed right***************************************")
motor.get_speed_right()
logging.info("**************************Speed left***************************************")
motor.get_speed_left()
