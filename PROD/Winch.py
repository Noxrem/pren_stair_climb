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

    def pull_up(self, speed=70):
        message = "mot setW " + str(speed)
        self.serial_access.write(message)
        time.sleep(5)
        while self.accelerometer.get_acceleration_z() > 9.9:  # TODO: define value
            logging.debug("pull up")
        logging.info("pulled up")
        message = "mot setW 0"
        self.serial_access.write(message)


