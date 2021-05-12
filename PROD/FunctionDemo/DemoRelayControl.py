import time as t
import RelayControl

relay_control = RelayControl.RelayControl()

while False:
    for i in range(1, 5):
        relay_control.set_on_relay(i)
        print(f'Main: Is relay {i} on ' + str(relay_control.is_relay_on(i)))
        t.sleep(1)
        relay_control.set_off_relay(i)
        print(f'Main: Is relay {i} on ' + str(relay_control.is_relay_on(i)))
        t.sleep(1)
