import serial
import time


class UARTAccess:
    access = None

    def __init__(self):
        print("create new UART access")
        self.access = serial.Serial("/dev/serial0", baudrate=57600, parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

    def write(self, message):
        print("UART write")
        self.access.write(str.encode(message))

    def write_and_read(self, message):
        print("UART write and read")
        self.write(message)
        time.sleep(0.5)  # TODO: define needed minimal duration
        while self.access.inWaiting() > 0:
            line = self.access.readline()
            print(line)