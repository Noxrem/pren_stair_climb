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
        while bigger_than_previous_counter < 4:  # TODO: define best value
            distance = self.ultrasonic_module_control.get_distance_in_cm(0)
            logging.info(str(distance) + " cm")
            if distance < 190:
                distances.append(distance)
                if distances.__getitem__(i) > distances.__getitem__(i - 1) + 0.2:
                    bigger_than_previous_counter += 1
                i += 1
            else:
                bigger_than_previous_counter = 0
        logging.info("stair detected")

    def find_stair_with_ultrasonic_v2(self):
        distances = list()
        distance = self.ultrasonic_module_control.get_distance_in_cm(0)
        min_target_amount = self._calculate_min_target_amount(distance)
        negative_counter = 0
        while len(distances) < min_target_amount:
            distance = self.ultrasonic_module_control.get_distance_in_cm(0)
            logging.info(str(distance) + " cm")
            if distance < 190:
                distances.append(distance)
                logging.info("Add distance to list")
            else:
                negative_counter += 1
                if negative_counter >= 3 and len(distances) != 0:
                    distances.clear()
                    logging.info("Reset")
        logging.info("stair detected")


    def _calculate_min_target_amount(self, distance):
        dynamic_counter = int(round(-0.074 * distance + 20.368, 0))  # values: 5cm -> 20 until 195cm ->  6
        logging.info("Dynamic Counter: " + str(dynamic_counter))
        return dynamic_counter
