# Copyright Nathanael Birrer HSLU

# Description
# Relay card control test function

# Imports
import time as t

import relayControl as relayCard

relayCard.init()

while True:
    for i in range(1, 5):
        relayCard.set_on_relay(i)
        print(f'Main: Is relay {i} on ' + str(relayCard.is_relay_on(i)))
        t.sleep(1)
        relayCard.set_off_relay(i)
        print(f'Main: Is relay {i} on ' + str(relayCard.is_relay_on(i)))
        t.sleep(1)
