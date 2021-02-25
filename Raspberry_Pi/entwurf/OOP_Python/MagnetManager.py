class MagnetManager:

    is_set_magnet_bridge = None
    is_set_magnet_socle = None

    def __init__(self):
        print("new MagnetManager created")
        self.is_set_magnet_socle = True
        self.is_set_magnet_bridge = True

    def get_available_arguments(self):
        command = "mag help"
        print(command)
        available_arguments = []
        # TODO Liste mit verfügbaren Argumenten befüllen
        return available_arguments

    def get_state_bridge(self):
        command = "mag state b"
        print(command)
        # TODO Status auslesen und zuweisen
        return self.is_set_magnet_bridge

    def set_on_power_bridge(self):
        command = "mag set b"
        print(command)

    def set_off_power_bridge(self):
        command = "mag off b"
        print(command)

    def get_state_socket(self):
        command = "mag state s"
        print(command)
        # TODO Status auslesen und zuweisen
        return self.is_set_magnet_socle

    def set_on_power_socket(self):
        command = "mag set s"
        print(command)

    def set_off_power_socket(self):
        command = "mag off s"
        print(command)



