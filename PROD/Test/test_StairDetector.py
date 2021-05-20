import StairDetector
from unittest import TestCase


# manual test

class TestStairDetector(TestCase):
    stair_detector = None

    def setUp(self):
        self.stair_detector = StairDetector.StairDetector()

    def test_constructor(self):
        self.assertIsNotNone(self.stair_detector)
