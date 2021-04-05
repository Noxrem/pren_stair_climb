import UARTAccess

# info: left = 0 degrees / ahead = 90 degrees / right = 180 degrees


class CamServo:
    degrees = None
    serial_access = None

    def __init__(self):
        print("new CamServo created")
        self.degrees = 90
        self.serial_access = UARTAccess.UARTAccess()

    def turn_ahead(self):
        if self.degrees != 90:
            print("turn cam servo ahead")
            message = "srv pta4 90"
            self.serial_access.write(message)
            self.degrees = 90
        else:
            print("cam servo is already turned ahead")

    def turn_right(self):
        if self.degrees != 180:
            print("turn cam servo right")
            message = "srv pta4 180"
            self.serial_access.write(message)
            self.degrees = 180
        else:
            print("cam servo is already turned right")

    def turn_left(self):
        if self.degrees != 0:
            print("turn cam servo left")
            message = "srv pta4 0"
            self.serial_access.write(message)
            self.degrees = 0
        else:
            print("cam servo is already turned left")

    def turn_one_degree_right(self):
        if self.degrees != 180:
            self.degrees = self.degrees + 1
            print("turn cam servo 1 degree right. Actual degrees: " + str(self.degrees))
            message = ("srv pta4 " + str(self.degrees))
            self.serial_access.write(message)

    def turn_one_degree_left(self):
        if self.degrees != 0:
            self.degrees = self.degrees - 1
            print("turn cam servo 1 degree left. Actual degrees: " + str(self.degrees))
            message = ("srv pta4 " + str(self.degrees))
            self.serial_access.write(message)
