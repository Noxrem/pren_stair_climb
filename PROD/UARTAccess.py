import serial


class UARTAccess:
    access = None

    def __init__(self):
        # TODO: delete first line & activate and adjust code
        print("create new UART access")
        # self.access = "Access"
        self.access = serial.Serial("/dev/serial0", baudrate=57600, parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

    def write(self, message):
        # TODO: activate code
        print("UART write")
        self.access.write(str.encode(message))

    def read(self):
        # TODO: activate code
        print("UART read")
        return self.access.read()
