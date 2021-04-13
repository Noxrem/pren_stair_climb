import UltrasonicModuleControl
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

ultrasonic_module_control = UltrasonicModuleControl.UltrasonicModuleControl()
while True:
    logging.info(ultrasonic_module_control.get_distance_in_cm())
