import Motor
import time

motor = Motor.Motor()
motor.enable()
motor.rotate(-100, -100)
time.sleep(3)
motor.stop()
motor.disable()
