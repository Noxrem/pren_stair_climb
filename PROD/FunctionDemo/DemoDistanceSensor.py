
import time
from RPi import GPIO
import UltrasonicModuleControl
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

ultrasonic_module_control = UltrasonicModuleControl.UltrasonicModuleControl()

try:
    # Calibrate sensor
    # ultrasonic_module_control.calibrate_sensors(distance_sensor_to_object=10) # used, if both sensors should be calibrated
    #ultrasonic_module_control.calibrate_sensor(ultrasonic_module_control.sensor_front, distance_sensor_to_object=10)
    while True:
        dist_1 = ultrasonic_module_control.get_distance_in_cm(0)  # 0 ist front sensor / 1 is side sensor
        logging.info("\nMeasured Distance = %.2f cm" % dist_1)
        time.sleep(0.3)

    # Reset by pressing CTRL + C
except (KeyboardInterrupt or IOError):
    print("Measurement stopped by User or IO Error occurred")
    GPIO.cleanup()

