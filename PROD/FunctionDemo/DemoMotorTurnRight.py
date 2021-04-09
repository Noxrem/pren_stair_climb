import Motor
import time

motor = Motor.Motor()
motor.enable()
motor.rotate(-30, 30)
time.sleep(5)
motor.stop()
motor.disable()
