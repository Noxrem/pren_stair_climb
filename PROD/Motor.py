import UARTAccess


class Motor:
    is_enabled = None
    serial_access = None

    def __init__(self):
        print("create new motor")
        self.is_enabled = False
        self.serial_access = UARTAccess.UARTAccess()

    def get_available_arguments(self):
        message = "mot help"
        available_arguments = []  # TODO Liste mit verfügbaren Argumenten befüllen
        return available_arguments

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

    # TODO: Spezifikation: UART Schnittstellenbefehle müssen um Argument 3 Drehdauer ergänzt werden
    def rotate(self, arg1_side, arg2_speed, arg3_duration_millisecond):
        message = "mot " + arg1_side + " " + arg2_speed + " " + arg3_duration_millisecond
        print(message)
