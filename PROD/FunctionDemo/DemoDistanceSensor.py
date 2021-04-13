import UltrasonicModuleControl

ultrasonic_module_control = UltrasonicModuleControl.UltrasonicModuleControl()
while True:
    print(ultrasonic_module_control.get_distance_in_cm())
