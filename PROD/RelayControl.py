# Imports
import logging
import sys
import smbus


class RelayControl:
    # Defines & Variables
    ON = None
    OFF = None
    DEVICE_BUS = None
    DEVICE_ADDR = None
    ARRAY_OFFSET = None
    bus = None
    relay_states = None

    # Functions
    def __init__(self):
        try:
            logging.info("RelayCard: Init all relays to OFF")
            self.ON = 0xFF
            self.OFF = 0x00
            self.DEVICE_BUS = 1
            self.DEVICE_ADDR = 0x10
            self.ARRAY_OFFSET = 1
            self.bus = smbus.SMBus(self.DEVICE_BUS)
            self.relay_states = [0, 0, 0, 0]
            for relay_number in range(1, 5):
                self.bus.write_byte_data(self.DEVICE_ADDR, relay_number, self.OFF)
                self.save_relay_state(relay_number, self.OFF)
        except IOError:
            logging.error("RelayCard: Init all relays to OFF failed")
            sys.exit()

    def set_on_relay(self, relay_number):
        try:
            logging.info("RelayCard: Set on relay " + str(relay_number))
            self.bus.write_byte_data(self.DEVICE_ADDR, relay_number, self.ON)
            self.save_relay_state(relay_number, self.ON)
        except IOError:
            logging.error("RelayCard: Set on relay failed " + str(relay_number))
            sys.exit()

    def set_off_relay(self, relay_number):
        try:
            logging.info("RelayCard: Set off relay " + str(relay_number))
            self.bus.write_byte_data(self.DEVICE_ADDR, relay_number, self.OFF)
            self.save_relay_state(relay_number, self.OFF)
        except IOError:
            logging.error("RelayCard: Set off relay failed " + str(relay_number))
            sys.exit()

    def is_relay_on(self, relay_number):
        if self.relay_states[relay_number - self.ARRAY_OFFSET] == self.ON:
            return True
        else:
            return False

    def save_relay_state(self, relay_number, relay_state):
        self.relay_states[relay_number - self.ARRAY_OFFSET] = relay_state
