import UARTAccess


class Winch:

    serial_access = None

    def __init__(self):
        print("Winch created")
        self.serial_access = UARTAccess.UARTAccess()

    def pull_up(self):
        print("pull up")
        message = ""  # TODO: define UART
        self.serial_access.write(message)
