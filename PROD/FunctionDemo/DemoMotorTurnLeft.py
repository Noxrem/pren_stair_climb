import Motor
import time

motor = Motor.Motor()
motor.enable()
motor.rotate(30, -30)
time.sleep(5)
motor.rotate(0, 0)
motor.disable()
