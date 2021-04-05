import serial


class UARTAccess:
    access = None

    def __init__(self):
        print("create new UART access")
        self.access = serial.Serial("/dev/serial0", baudrate=57600, parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

    def write(self, message):
        print("UART write")
        self.access.write(str.encode(message))

    def read(self):
        print("UART read")
        return self.access.readline()

    def write_and_read(self, message):
        print("UART write and read")
        self.write(message)
        is_data_available = True
        while is_data_available:
            line = self.read()
            if line == "":
                is_data_available = False
            else:
                print(line)
