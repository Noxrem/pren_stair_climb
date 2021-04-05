import Robot
import time

robot = Robot.Robot("Gefyra")
robot.go_forward_slow()
time.sleep(3)
robot.go_backward_slow()
time.sleep(3)
robot.turn_right()
time.sleep(5)
robot.turn_left()
time.sleep(5)
robot.motor_wheels.disable()
