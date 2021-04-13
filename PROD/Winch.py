import UARTAccess
import Accelerometer
import time
import logging


class Winch:

    serial_access = None
    accelerometer = None

    def __init__(self):
        logging.info("create new Winch")
        self.serial_access = UARTAccess.UARTAccess()
        self.accelerometer = Accelerometer.Accelerometer()

    def pull_up(self, speed):
        message = "mot setW " + str(speed)
        self.serial_access.write(message)
        time.sleep(5)
        while True:
            if self.accelerometer.get_acceleration_z_direction() == 0:
                logging.info("pulled up")
                break

    def pull_up_fast(self):
        logging.info("pull up fast")
        self.pull_up(100)

    def pull_up_slow(self):
        logging.info("pull up slow")
        self.pull_up(30)



