import UltrasonicModuleControl
import logging

ultrasonic_module_control = UltrasonicModuleControl.UltrasonicModuleControl()
while True:
    logging.info(ultrasonic_module_control.get_distance_in_cm())
