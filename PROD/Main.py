import Robot
import TargetPlatform

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


robot = Robot.Robot("Gefyra")
target_plattform = TargetPlatform.TargetPlatform()
target_plattform.print_pictogram_order()
robot.turn_and_find_pictogram(True)
robot.turn_and_find_stair(False)
robot.go_forward_and_get_distance()

logging.info("************************End of program********************************")
