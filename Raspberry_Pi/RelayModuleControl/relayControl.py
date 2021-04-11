# Copyright Nathanael Birrer HSLU

# Description
# Relay card control

# Useful links
# Shop: https://www.seeedstudio.com/DockerPi-4-Channel-Relay-p-4096.html
# Code example: https://wiki.52pi.com/index.php/DockerPi_4_Channel_Relay_SKU:_EP-0099
# Remote debug: https://www.youtube.com/watch?v=oikrc1lEMXg&ab_channel=szparacha
# Python version: https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux
# RPi4 pinout: https://www.raspberrypi.org/documentation/usage/gpio/

# Prerequisites
# python -m pip install smbus

# Imports
import sys
import smbus

# Defines & Variables
ON = 0xFF
OFF = 0x00
DEVICE_BUS = 1
DEVICE_ADDR = 0x10
ARRAY_OFFSET = 1
bus = smbus.SMBus(DEVICE_BUS)
relay_states = [0, 0, 0, 0]



# Functions
def init():
    try:
        print("RelayCard: Init all relays to OFF")
        for relay_number in range(1, 5):
            bus.write_byte_data(DEVICE_ADDR, relay_number, OFF)
            save_relay_state(relay_number, OFF)
    except IOError:
        print("RelayCard: Init all relays to OFF failed")
        sys.exit()


def set_on_relay(relay_number):
    try:
        print("RelayCard: Set on relay " + str(relay_number))
        bus.write_byte_data(DEVICE_ADDR, relay_number, ON)
        save_relay_state(relay_number, ON)
    except IOError:
        print("RelayCard: Set on relay failed " + str(relay_number))
        sys.exit()


def set_off_relay(relay_number):
    try:
        print("RelayCard: Set off relay " + str(relay_number))
        bus.write_byte_data(DEVICE_ADDR, relay_number, OFF)
        save_relay_state(relay_number, OFF)
    except IOError:
        print("RelayCard: Set off relay failed " + str(relay_number))
        sys.exit()


def is_relay_on(relay_number):
    if relay_states[relay_number - ARRAY_OFFSET] == ON:
        return True
    else:
        return False


def save_relay_state(relay_number, relay_state):
    relay_states[relay_number - ARRAY_OFFSET] = relay_state
