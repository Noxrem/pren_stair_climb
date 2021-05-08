import Robot
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


robot = Robot.Robot("Gefyra")
robot.stair_detector_with_ultrasonic()
