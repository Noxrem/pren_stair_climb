import logging

import Robot

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

robot = Robot.Robot("DetectorRobot")
robot.object_detector.find_pictogram_start_platform(robot.camera)
