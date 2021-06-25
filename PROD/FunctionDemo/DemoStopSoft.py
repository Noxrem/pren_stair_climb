import Robot
import time

robot = Robot.Robot("test")
robot.go_forward_fast()
time.sleep(2)
robot.stop_soft(200)
robot.dispose()