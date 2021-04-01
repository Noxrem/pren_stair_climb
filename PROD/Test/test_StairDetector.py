import StairDetector
from unittest import TestCase


# manual test

class TestStairDetector((TestCase)):
    stair_detector = None

    def setUp(self):
        self.stair_detector = StairDetector.StairDetector()

    def test_constructor(self):
        self.assertIsNotNone(self.stair_detector)

    # this one has to be tested manually. As soon as 3 windows appears -> ok
    def test_find_stair(self):
        self.stair_detector.find_stair()
