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
        logging.info(str(self.accelerometer.get_acceleration_x()))
        message = "mot setW " + str(speed)
        self.serial_access.write(message)
        time.sleep(10)
        while self.accelerometer.get_acceleration_x() < 9.81:  # TODO: define value
            message = self.accelerometer.get_acceleration_x()
            logging.info("pull up")
            logging.info(str(message))
            time.sleep(0.5)
        logging.info("pulled up")
        message = "mot setW 0"
        self.serial_access.write(message)

    def pull_to_end(self, speed, duration):
        message = "mot setW " + str(speed)
        self.serial_access.write(message)
        time.sleep(duration)
        message = "mot setW 0"
        self.serial_access.write(message)
