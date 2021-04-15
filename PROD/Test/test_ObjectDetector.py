import unittest
import ObjectDetector


class TestObjectDetector(unittest.TestCase):
    object_detector = None

    def setUp(self):
        self.object_detector = ObjectDetector.ObjectDetector()

    def test_init_haar_cascade(self):
        self.object_detector = self.object_detector


if __name__ == '__main__':
    unittest.main()
