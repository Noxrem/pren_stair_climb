import Robot
import time

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

logging.info("************************Start of program********************************")

start_time = time.time()
logging.info("Main - Init Robot")
robot = Robot.Robot("Gefyra")
#robot.go_forward_and_stop_after_duration(70, Robot.calculate_duration(70, 300))
# robot.turn_and_find_pictogram(True)
# robot.speaker.play_text(robot.found_pictogram)
robot.turn_and_find_stair(False, True)
#vrobot.go_forward_and_get_distance()
# robot.do_alignment()
# robot.go_to_drop_off_position()
# robot.let_socket_down()
# robot.let_bridge_down()
# robot.pull_up()
# robot.pull_to_bridge_drop_off()
# robot.go_forward_and_stop_after_duration(50, Robot.calculate_duration(50, 400))  # todo: measure distance
robot.celebrate(robot.found_pictogram, time.time() - start_time)

logging.info("************************End of program********************************")
