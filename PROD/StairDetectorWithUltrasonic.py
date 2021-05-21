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
        negative_counter = 0
        bigger_than_previous_counter = 0
        while bigger_than_previous_counter < 10:  # TODO: define best value
            distance = self.ultrasonic_module_control.get_distance_in_cm(0)
            logging.info(str(distance) + " cm")
            if distance < 190:
                distances.append(distance)
                logging.info("added on index "+ str(i))
                if distances.__getitem__(i) > distances.__getitem__(i - 1) + 0.1:
                    bigger_than_previous_counter += 1
                i += 1
            else:
                negative_counter += 1
                if negative_counter >= 6:
                    bigger_than_previous_counter = 0
                    negative_counter = 0
        logging.info("stair detected")
        return 6

    def find_stair_with_ultrasonic_v2(self):
        distances = list()
        is_min_target_amount_set = False
        negative_counter = 0
        min_target_amount = 1000
        positive_counter = 0
        while len(distances) < min_target_amount:
            distance = self.ultrasonic_module_control.get_distance_in_cm(0)
            if not is_min_target_amount_set and distance < 190:
                min_target_amount = self._calculate_min_target_amount(distance)
                is_min_target_amount_set = True
                logging.info("target amount of measurements below 190 cm is: " + str(min_target_amount))
            logging.info(str(distance) + " cm")
            if distance < 190:
                distances.append(distance)
                positive_counter += 1
                logging.info("Add distance to list. positive_counter is: " + str(positive_counter) + " \ " + str(min_target_amount))
            else:
                negative_counter += 1
                if negative_counter >= 5:
                    logging.info("negative counter: " + str(negative_counter))
                    distances.clear()
                    positive_counter = 0
                    negative_counter = 0
                    is_min_target_amount_set = False
                    logging.info("Reset")
        logging.info("stair detected")
        return min_target_amount


    def _calculate_min_target_amount(self, distance):
        dynamic_counter = int(round(-0.079 * distance + 27.395))  # best values: 5cm -> 27 until 195cm ->  12 => b = 27.395, a = -0.079
        logging.info("Dynamic Counter: " + str(dynamic_counter))
        return dynamic_counter
