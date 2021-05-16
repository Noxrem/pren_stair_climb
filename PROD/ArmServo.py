import UARTAccess
import logging


class CamServo:
    degrees = None
    serial_access = None

    def __init__(self):
        logging.info("create new ArmServo")
        self.degrees = 180
        self.serial_access = UARTAccess.UARTAccess()

#  TODO: define degrees

    def turn_down(self):
        if self.degrees != 90:
            logging.info("turn arm servo down")
            message = "srv arm 90"
            self.serial_access.write(message)
            self.degrees = 90
        else:
            logging.warning("arm servo is already turned down")

    def turn_up(self):
        if self.degrees != 180:
            logging.info("turn arm servo up")
            message = "srv arm 180"
            self.serial_access.write(message)
            self.degrees = 180
        else:
            logging.warning("arm servo is already turned up")
