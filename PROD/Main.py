import logging
import Robot
import time
import traceback
from RPi import GPIO
from time import sleep

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

logging.info("************************Start of program********************************")

GPIO_PIN_START_BUTTON = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN_START_BUTTON, GPIO.IN, GPIO.PUD_UP)
button_not_pressed = True

logging.info("Main - Init Robot")
robot = Robot.Robot("Gefyra")

logging.info("**************waiting for start button************")
while button_not_pressed:  # this will carry on until you hit CTRL+C
    button_not_pressed = GPIO.input(GPIO_PIN_START_BUTTON)
    sleep(0.1)

start_time = time.time()

try:

    # robot.let_bridge_down()  # TODO: Only for test runs to save power
    # robot.let_socket_down()  # TODO: Only for test runs to save power

    robot.go_forward_and_stop_after_duration(70, Robot.calculate_duration_length_in_mm(70, 300))
    robot.turn_and_find_pictogram(True)
    robot.speaker.play_text(robot.found_pictogram)
    robot.turn_and_find_stair_only_with_ultrasonic()
    robot.find_stair(True)
    robot.go_forward_and_get_distance()
    robot.do_alignment()
    robot.go_to_drop_off_position()
    robot.let_bridge_down()
    robot.go_forward_and_stop_after_duration(50, 1)
    robot.go_forward_and_stop_after_duration(400, 1)
    robot.go_backward_and_stop_after_duration(400, 1)
    robot.go_backward_and_stop_after_duration(50, 1)
    robot.let_socket_down()
    time.sleep(2)
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
