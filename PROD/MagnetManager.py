
class MagnetManager:
    is_switched_on_magnet_bridge = None
    is_switched_on_magnet_socket = None
    serial_access = None

    def __init__(self):
        print("create new MagnetManager")
        self.is_switched_on_magnet_socket = False
        self.is_switched_on_magnet_bridge = False

    def set_on_power_bridge(self):
        if not self.is_switched_on_magnet_bridge:
            print("set on power bridge")
            self.is_switched_on_magnet_bridge = True
            # TODO: Nathi: Implementation
        else:
            print("magnet for the bridge is already switched on")

    def set_off_power_bridge(self):
        if self.is_switched_on_magnet_bridge:
            print("set off power bridge")
            self.is_switched_on_magnet_bridge = False
            # TODO: Nathi: Implementation
        else:
            print("magnet for the bridge is already switched off")

    def set_on_power_socket(self):
        if not self.is_switched_on_magnet_socket:
            print("set on power socket")
            self.is_switched_on_magnet_socket = True
            # TODO: Nathi: Implementation
        else:
            print("magnet for the socket is already switched on")

    def set_off_power_socket(self):
        if self.is_switched_on_magnet_socket:
            print("set off power socket")
            self.is_switched_on_magnet_socket = False
            # TODO: Nathi: Implementation
        else:
            print("magnet for the socket is already switched off")
