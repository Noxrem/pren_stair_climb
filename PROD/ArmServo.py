import UARTAccess
import logging


class ArmServo:
    degrees = None
    serial_access = None

    def __init__(self):
        logging.info("create new ArmServo")
        self.serial_access = UARTAccess.UARTAccess()
        self.turn_up()
        self.degrees = 30


#  TODO: define degrees

    def turn_down(self):
            logging.info("turn arm servo down")
            message = "srv arm 150"
            self.serial_access.write(message)
            self.degrees = 150

    def turn_up(self):
            logging.info("turn arm servo up")
            message = "srv arm 30"
            self.serial_access.write(message)
            self.degrees = 30
