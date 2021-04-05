import Winch
import Motor

motor = Motor.Motor()
motor.enable()
winch = Winch.Winch()
winch.pull_up_slow()
motor.disable()