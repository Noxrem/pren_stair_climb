import logging
import RelayControl

class MagnetManager:
    relay_control = None
    is_switched_on_magnet_bridge = None
    is_switched_on_magnet_socket = None

    def __init__(self):
        logging.info("create new MagnetManager")
        self.relay_control = RelayControl.RelayControl()
        self.is_switched_on_magnet_socket = False
        self.is_switched_on_magnet_bridge = False

    def set_on_power_bridge(self):
        if not self.is_switched_on_magnet_bridge:
            logging.info("magnet manager: set on power bridge")
            self.is_switched_on_magnet_bridge = True
            self.relay_control.set_on_relay(1)
        else:
            logging.info("magnet for the bridge is already switched on")

    def set_off_power_bridge(self):
        if self.is_switched_on_magnet_bridge:
            logging.info("magnet manager: set off power bridge")
            self.is_switched_on_magnet_bridge = False
            self.relay_control.set_off_relay(1)
        else:
            logging.info("magnet for the bridge is already switched off")

    def set_on_power_socket(self):
        if not self.is_switched_on_magnet_socket:
            logging.info("magnet manager: set on power socket")
            self.is_switched_on_magnet_socket = True
            self.relay_control.set_on_relay(2)
            self.relay_control.set_on_relay(3)
        else:
            logging.info("magnet for the socket is already switched on")

    def set_off_power_socket(self):
        if self.is_switched_on_magnet_socket:
            logging.info("magnet manager: set off power socket")
            self.is_switched_on_magnet_socket = False
            self.relay_control.set_off_relay(2)
            self.relay_control.set_off_relay(3)
        else:
            logging.info("magnet for the socket is already switched off")
