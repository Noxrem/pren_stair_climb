import logging

class MagnetManager:
    is_switched_on_magnet_bridge = None
    is_switched_on_magnet_socket = None

    def __init__(self):
        logging.info("create new MagnetManager")
        self.is_switched_on_magnet_socket = False
        self.is_switched_on_magnet_bridge = False

    def set_on_power_bridge(self):
        if not self.is_switched_on_magnet_bridge:
            logging.info("set on power bridge")
            self.is_switched_on_magnet_bridge = True
            # TODO: Nathi: Implementation
        else:
            logging.info("magnet for the bridge is already switched on")

    def set_off_power_bridge(self):
        if self.is_switched_on_magnet_bridge:
            logging.info("set off power bridge")
            self.is_switched_on_magnet_bridge = False
            # TODO: Nathi: Implementation
        else:
            logging.info("magnet for the bridge is already switched off")

    def set_on_power_socket(self):
        if not self.is_switched_on_magnet_socket:
            logging.info("set on power socket")
            self.is_switched_on_magnet_socket = True
            # TODO: Nathi: Implementation
        else:
            logging.info("magnet for the socket is already switched on")

    def set_off_power_socket(self):
        if self.is_switched_on_magnet_socket:
            logging.info("set off power socket")
            self.is_switched_on_magnet_socket = False
            # TODO: Nathi: Implementation
        else:
            logging.info("magnet for the socket is already switched off")
