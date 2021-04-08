import UARTAccess


class Motor:
    is_enabled = None
    serial_access = None

    def __init__(self):
        print("create new motor")
        self.is_enabled = False
        self.serial_access = UARTAccess.UARTAccess()

    def drive_help(self):
        message = "drv help"
        print(message)
        self.serial_access.write_and_read(message)

    def motor_help(self):
        message = "mot help"
        print(message)
        self.serial_access.write_and_read(message)

    def enable(self):
        if not self.is_enabled:
            message = "mot enable"
            print(message)
            self.serial_access.write(message)
            self.is_enabled = True
        else:
            print("motor is already enabled")

    def disable(self):
        if self.is_enabled:
            message = "mot disable"
            print(message)
            self.serial_access.write(message)
            self.is_enabled = False
        else:
            print("motor is already disabled")

    def rotate(self, speed_right, speed_left):
        message = "drv " + "setSpd " + str(speed_right) + " " + str(speed_left)
        self.serial_access.write_and_read(message)
        print(message)

    def stop(self):
        message = "drv " + "setSpd " + str(0) + " " + str(0)
        self.serial_access.write(message)
        print(message)

    def get_speed_right(self):
        message = "q " + "getSpdR"
        self.serial_access.write_and_read(message)

    def get_speed_left(self):
        message = "q " + "getSpdL"
        self.serial_access.write_and_read(message)

