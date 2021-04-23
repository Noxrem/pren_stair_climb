import logging
import Robot

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

robot = Robot.Robot("Gefyra")
robot.go_to_drop_off_position()
