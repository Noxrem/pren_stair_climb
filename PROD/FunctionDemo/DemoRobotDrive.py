import Robot
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


robot = Robot.Robot("Gefyra")
robot.go_forward_slow()
time.sleep(3)
robot.go_backward_slow()
time.sleep(3)
robot.turn_right()
time.sleep(5)
robot.turn_left()
time.sleep(5)
robot.stop()
robot.motor_wheels.disable()
