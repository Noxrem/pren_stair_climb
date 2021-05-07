import serial
import time
import logging

timeout_to_read = 0.1  # TODO: define needed minimal duration


class UARTAccess:
    access = None

    def __init__(self):
        logging.info("create new UART access")
        self.access = serial.Serial("/dev/serial0", baudrate=57600, parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

    def write(self, message):
        logging.info("UART write")
        formatted_message = message + str("\n")
        self.access.write(str.encode(formatted_message))

    def read(self):
        logging.info("UART read line")
        time.sleep(timeout_to_read)
        data = b''                              # Create empty bytes type
        while self.access.inWaiting() > 0:
            line = self.access.readline()
            if len(line) > 0:
                logging.info(line)
                data += line
        return data

    def write_and_read(self, message):
        logging.info("UART write and read")
        self.write(message)
        data = self.read()
        return data