import CamServo
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


servo = CamServo.CamServo()
logging.info("********************servo turn up*********************")
servo.turn_up()
time.sleep(5)
logging.info("********************servo turn ahead*********************")
servo.turn_ahead()
time.sleep(5)
logging.info("********************servo turn down*********************")
servo.turn_down()
time.sleep(5)
logging.info("********************servo turn ahead*********************")
servo.turn_ahead()
time.sleep(5)
logging.info("********************servo turn 10 times 1 degree up**********************")
for i in range(10):
    servo.turn_to_degree()
logging.info("********************servo turn 10 times 1 degree down**********************")
for i in range(10):
    servo.turn_one_degree_down()

