import UARTAccess
import logging


class Motor:
    is_enabled = None
    serial_access = None

    def __init__(self):
        logging.info("create new motor")
        self.is_enabled = False
        self.serial_access = UARTAccess.UARTAccess()

    def drive_help(self):
        message = "drv help"
        logging.info(message)
        self.serial_access.write_and_read(message)

    def motor_help(self):
        message = "mot help"
        logging.info(message)
        self.serial_access.write_and_read(message)

    def enable(self):
        if not self.is_enabled:
            message = "mot enable"
            logging.info(message)
            self.serial_access.write(message)
            self.is_enabled = True
        else:
            logging.warning("motor is already enabled")

    def disable(self):
        if self.is_enabled:
            message = "mot disable"
            logging.info(message)
            self.serial_access.write(message)
            self.is_enabled = False
        else:
            logging.warning("motor is already disabled")

    def rotate(self, speed_right, speed_left):
        message = "drv " + "setSpd " + str(speed_right) + " " + str(speed_left)
        self.serial_access.write(message)
        logging.info(message)

    def stop(self):
        message = "drv " + "setSpd " + str(0) + " " + str(0)
        self.serial_access.write(message)
        logging.info(message)

    def get_speed_right(self):
        message = "q " + "getSpdR"
        self.serial_access.write_and_read(message)

    def get_speed_left(self):
        message = "q " + "getSpdL"
        self.serial_access.write_and_read(message)

