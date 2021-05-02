import logging
import Robot

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

robot = Robot.Robot("manuel")
robot.go_to_drop_off_position()

