import serial


class UARTAccess:
    access = None

    def __init__(self):
        # TODO: delete first line & activate and adjust code
        print("new UART access created")
        self.access = "Access"
        # self.access = serial.Serial("/dev/ttyS0", baudrate=9600, parity=serial.PARITY_NONE,
        #                            stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

    def write(self, message):
        # TODO: activate code
        print("UART write")
        # self.access.write(message)

    def read(self):
        # TODO: activate code
        print("UART read")
        self.access.read()
