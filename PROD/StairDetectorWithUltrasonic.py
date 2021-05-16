import time
import logging
import UltrasonicModuleControl


class StairDetectorWithUltrasonic:

    def __init__(self):
        logging.info("create new StairDetectorWithUltrasonic")
        self.ultrasonic_module_control = UltrasonicModuleControl.UltrasonicModuleControl()

    def find_stair_with_ultrasonic(self):
        distances = list()
        i = 0
        bigger_than_previous_counter = 0
        while bigger_than_previous_counter < 10:  # TODO: define best value
            distance = self.ultrasonic_module_control.get_distance_in_cm(0)
            logging.info(str(distance) + " cm")
            if distance < 190:
                logging.info(str(distance) + " cm")
                distances.append(distance)
                if distances.__getitem__(i) > distances.__getitem__(i - 1):
                    bigger_than_previous_counter += 1
                i += 1
            time.sleep(0.2)
