import Robot
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


robot = Robot.Robot("DemoRobot")

while True:
    robot.turn_and_find_stair(True)
