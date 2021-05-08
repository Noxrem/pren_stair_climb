import logging
import time
import Accelerometer

accelerometer = Accelerometer.Accelerometer()

while True:
    logging.info("movement in direction x is: {}", accelerometer.get_acceleration_x())
    logging.info("movement in direction y is: {}", accelerometer.get_acceleration_y())
    logging.info("movement in direction z is: {}", accelerometer.get_acceleration_z())
    logging.info("is it hot in here?: {}", accelerometer.get_temperature_in_celsius())
    time.sleep(1)
