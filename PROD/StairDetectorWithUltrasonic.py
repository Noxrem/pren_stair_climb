import time
import logging
import UltrasonicModuleControl


class StairDetectorWithUltrasonic:

    def __init__(self):
        logging.info("create new StairDetectorWithUltrasonic")
        self.ultrasonic_module_control = UltrasonicModuleControl.UltrasonicModuleControl()

    def find_stair_with_ultrasonic(self):
        distances = list()
        distance = self.ultrasonic_module_control.get_distance_in_cm(0)
        distances.append(distance)
        i = 0
        bigger_than_previous_counter = 0
        counter_negative = 0
        dynamic_counter = 5
        while bigger_than_previous_counter < dynamic_counter:  # TODO: define best value
            distance = self.ultrasonic_module_control.get_distance_in_cm(0)
            logging.info(str(distance) + " cm")
            if distance < 190:
                if distance > distances.__getitem__(i) + 0.2:
                    distances.append(distance)
                    i += 1
                    bigger_than_previous_counter += 1
                    logging.info("bigger_than_previous_counter: "  + str(bigger_than_previous_counter))
                    dynamic_counter = self.get_amount_counter(distances.__getitem__(i))
                    logging.info("dynamic counter: " + str(dynamic_counter))
                elif distance < distances.__getitem__(i) - 0.2:
                    counter_negative += 1
                    logging.info("negative counter: " + str(counter_negative))
                    if counter_negative >= 4:
                        logging.info("Reset counters")
                        bigger_than_previous_counter = 0
                        counter_negative = 0
            else:
                counter_negative = 0
                bigger_than_previous_counter = 0
        logging.info("stair detected")


    def get_amount_counter(self, distance):
        dynamic_counter = round(-0.115 * distance + 22.308, 0)
        # if dynamic_counter < 5:
        #    dynamic_counter = 5
        logging.info("Dynamic Counter: " + str(dynamic_counter))
        return dynamic_counter

