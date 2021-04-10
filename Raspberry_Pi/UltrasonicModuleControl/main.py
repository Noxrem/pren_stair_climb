# Copyright Nathanael Birrer HSLU

# Description
# Ultrasonic module control test
import time
from RPi import GPIO
import UltrasonicModuleControl as ultrasonicModule

try:
    # Calibrate sensor
    ultrasonicModule.calibrate_sensors(distance_sensor_to_object=10)
    while True:
        dist_1 = ultrasonicModule.get_distance_in_cm()
        print("\nMeasured Distance = %.2f cm" % dist_1)
        time.sleep(0.3)

    # Reset by pressing CTRL + C
except (KeyboardInterrupt or IOError):
    print("Measurement stopped by User or IO Error occurred")
    GPIO.cleanup()

