import serial


class UARTAccess:
    access = None

    def __init__(self):
        # TODO:  Activate the line below and delete the line after the next line (is not working on laptop)
        self.access = serial.Serial("/dev/ttyS0", 9600)

    def write(self, message):
        self.access.write(message)

    def read(self):
        self.access.read()

