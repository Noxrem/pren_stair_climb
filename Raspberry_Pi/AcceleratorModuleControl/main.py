# Copyright Nathanael Birrer HSLU

# Description
# Accelerator module test

import time
import AcceleratorModuleControl

try:
    while True:
        print("Acceleration X: %.2f" % AcceleratorModuleControl.get_acceleration_x())
        print("Acceleration Y: %.2f" % AcceleratorModuleControl.get_acceleration_y())
        print("Acceleration Z: %.2f" % AcceleratorModuleControl.get_acceleration_z())
        print("Temperature: %.2f C" % AcceleratorModuleControl.get_temperature_in_celsius())
        print("")
        time.sleep(1)

    # Reset by pressing CTRL + C
except (KeyboardInterrupt or IOError):
    print("Measurement stopped by User or IO Error occurred")

