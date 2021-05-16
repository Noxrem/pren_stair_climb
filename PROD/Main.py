import logging
import traceback
import Robot
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

logging.info("************************Start of program********************************")

start_time = time.time()

logging.info("Main - Init Robot")
robot = Robot.Robot("Gefyra")
time.sleep(5)

try:

    robot.let_bridge_down()  # TODO: Only for test runs to save power
    robot.let_socket_down()  # TODO: Only for test runs to save power

    robot.go_forward_and_stop_after_duration(70, Robot.calculate_duration_length_in_mm(70, 300))
    robot.turn_and_find_pictogram(True)
    robot.speaker.play_text(robot.found_pictogram)
    robot.turn_and_find_stair(False, True)
    robot.go_forward_and_get_distance()
    robot.do_alignment()
    robot.go_to_drop_off_position()
    robot.let_bridge_down()
    time.sleep(20)
    robot.go_forward_and_stop_after_duration(400, 1)
    robot.go_backward_and_stop_after_duration(400, 1)
    robot.let_socket_down()
    robot.go_forward_fast()
    robot.pull_up()
    robot.pull_to_bridge_drop_off()
    robot.turn_arm_down()
    robot.go_forward_and_stop_after_duration(50, Robot.calculate_duration_length_in_mm(50, 400))  # todo: measure distance
    robot.celebrate(robot.found_pictogram, time.time() - start_time)
    robot.dispose()

except Exception as ex:
    logging.error("Error occurred. Programm is canceled:")
    logging.error(traceback.print_exc())
    logging.info("Robot dispose")
    robot.dispose()

logging.info("************************End of program********************************")
