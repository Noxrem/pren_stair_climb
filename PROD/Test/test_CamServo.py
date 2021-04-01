from unittest import TestCase
import CamServo


class TestCamServo(TestCase):

    def setUp(self):
        self.cam_servo = CamServo.CamServo()

    def test_turn_ahead(self):
        self.cam_servo.turn_ahead()
        self.assertTrue(self.cam_servo.is_ahead)

    def test_turn_right(self):
        self.cam_servo.turn_right()
        self.assertFalse(self.cam_servo.is_ahead)
