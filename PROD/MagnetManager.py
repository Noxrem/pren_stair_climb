import UARTAccess


class MagnetManager:
    is_switched_on_magnet_bridge = None
    is_switched_on_magnet_socket = None
    serial_access = None

    def __init__(self):
        print("new MagnetManager created")
        self.is_switched_on_magnet_socket = True
        self.is_switched_on_magnet_bridge = True
        self.serial_access = UARTAccess.UARTAccess()

    def get_available_arguments(self):
        message = "mag help"
        print(message)
        available_arguments = []
        # TODO Liste mit verfügbaren Argumenten befüllen
        return available_arguments

    def get_state_bridge(self):
        message = "mag state b"
        print(message)
        # TODO Status auslesen und zuweisen
        return self.is_switched_on_magnet_bridge

    def set_on_power_bridge(self):
        if not self.is_switched_on_magnet_bridge:
            message = "mag set b"
            print(message)
            self.serial_access.write(message)
            self.is_switched_on_magnet_bridge = True
        else:
            print("magnet for the bridge is already switched on")

    def set_off_power_bridge(self):
        if self.is_switched_on_magnet_bridge:
            message = "mag off b"
            print(message)
            self.serial_access.write(message)
            self.is_switched_on_magnet_bridge = False
        else:
            print("magnet for the bridge is already switched off")

    def get_state_socket(self):
        message = "mag state s"
        print(message)
        # TODO Status auslesen und zuweisen
        return self.is_switched_on_magnet_socket

    def set_on_power_socket(self):
        if not self.is_switched_on_magnet_bridge:
            message = "mag set s"
            print(message)
            self.serial_access.write(message)
            self.is_switched_on_magnet_socket = True
        else:
            print("magnet for the socket is already switched on")

    def set_off_power_socket(self):
        if self.is_switched_on_magnet_bridge:
            message = "mag off s"
            print(message)
            self.serial_access.write(message)
            self.is_switched_on_magnet_socket = False
        else:
            print("magnet for the socket is already switched off")
