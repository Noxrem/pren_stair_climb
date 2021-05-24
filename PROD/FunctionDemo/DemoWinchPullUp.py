import Winch
import Motor
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


motor = Motor.Motor()
motor.enable()
winch = Winch.Winch()
winch.pull_up(50)
motor.disable()
