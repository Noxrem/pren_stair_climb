import CamServo
import time
import logging

servo = CamServo.CamServo()
logging.info("********************servo turn left*********************")
servo.turn_left()
time.sleep(5)
logging.info("********************servo turn ahead*********************")
servo.turn_ahead()
time.sleep(5)
logging.info("********************servo turn left*********************")
servo.turn_right()
time.sleep(5)
logging.info("********************servo turn ahead*********************")
servo.turn_ahead()
time.sleep(5)
logging.info("********************servo turn 10 times 1 degree left**********************")
for i in range(10):
    servo.turn_one_degree_left()
logging.info("********************servo turn 10 times 1 degree right**********************")
for i in range(10):
    servo.turn_one_degree_right()

