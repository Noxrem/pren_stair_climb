class Motor:

    def __init__(self):
        print("new motor created")

    def get_available_arguments(self):
        command = "mot help"
        available_arguments = []
        return available_arguments

    def enable(self):
        command = "mot enable"

    def disable(self):
        command = "mot disable"

    # TODO: Spezifikation: UART Schnittstellenbefehle müssen um Argument 3 Drehdauer ergänzt werden

    def rotate(self, arg1_side, arg2_speed, arg3_duration_millisecond):
        command = "mot " + arg1_side + " " + arg2_speed + " " + arg3_duration_millisecond
        print(command)
