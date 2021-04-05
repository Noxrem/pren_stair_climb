import UARTAccess
import Accelerometer
import time


class Winch:

    serial_access = None
    accelerometer = None

    def __init__(self):
        print("create new Winch")
        self.serial_access = UARTAccess.UARTAccess()
        self.accelerometer = Accelerometer.Accelerometer()

    def pull_up(self, speed):
        message = "mot setW " + str(speed)
        self.serial_access.write(message)
        time.sleep(5)
        while True:
            if self.accelerometer.get_acceleration_z_direction() == 0:
                print("pulled up")
                break

    def pull_up_fast(self):
        print("pull up fast")
        self.pull_up(100)

    def pull_up_slow(self):
        print("pull up slow")
        self.pull_up(30)



