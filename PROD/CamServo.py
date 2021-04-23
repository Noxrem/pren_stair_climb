import UARTAccess
import logging


class CamServo:
    degrees = None
    serial_access = None

    def __init__(self):
        logging.info("create new CamServo")
        self.degrees = 90
        self.serial_access = UARTAccess.UARTAccess()

#  TODO: define degrees

    def turn_ahead(self):
        if self.degrees != 90:
            logging.info("turn cam servo ahead")
            message = "srv pta4 90"
            self.serial_access.write(message)
            self.degrees = 90
        else:
            logging.warning("cam servo is already turned ahead")

    def turn_up(self):
        if self.degrees != 180:
            logging.info("turn cam servo up")
            message = "srv pta4 180"
            self.serial_access.write(message)
            self.degrees = 180
        else:
            logging.warning("cam servo is already turned up")

    def turn_down(self):
        if self.degrees != 0:
            logging.info("turn cam servo down")
            message = "srv pta4 0"
            self.serial_access.write(message)
            self.degrees = 0
        else:
            logging.warning("cam servo is already turned down")

    def turn_to_degree(self, degrees):
        if self.degrees != 180:
            self.degrees = degrees
            logging.info("turn cam servo 1 degree up. Actual degrees: " + str(self.degrees))
            message = ("srv pta4 " + str(self.degrees))
            self.serial_access.write(message)
        else:
            logging.warning("cam servo is already turned up")
