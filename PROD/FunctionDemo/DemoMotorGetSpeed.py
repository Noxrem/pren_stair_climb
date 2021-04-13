import Motor
import logging

motor = Motor.Motor()
logging.info("**************************Speed right***************************************")
motor.get_speed_right()
logging.info("**************************Speed left***************************************")
motor.get_speed_left()
