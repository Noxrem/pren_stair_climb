import UARTAccess


class CamServo:
    is_ahead = None
    serial_access = None

    def __init__(self):
        self.is_ahead = True
        self.serial_access = UARTAccess.UARTAccess()

    def turn_ahead(self):
        if not self.is_ahead:
            print("turn cam servo ahead")
            message = ""  # TODO: define UART
            self.serial_access.write(message)
            self.is_ahead = True
        else:
            print("cam servo is already turned ahead")

    def turn_right(self):
        if self.is_ahead:
            print("turn cam servo ahead")
            message = ""  # TODO: define UART
            self.serial_access.write(message)
            self.is_ahead = False
        else:
            print("cam servo is already turned right")
