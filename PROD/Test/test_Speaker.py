from unittest import TestCase
import Speaker


class TestSpeaker(TestCase):
    speaker = None
    found_pictogram1 = "None"

    def setUp(self):
        self.speaker = Speaker.Speaker()
        self.found_pictogram1 = "sandwich"

    def test_play_text(self):
        self.speaker.play_text(self.found_pictogram1)

    # Attention: duration of this test is about 3 min
    def test_celebrate(self):
        self.speaker.celebrate(self.found_pictogram1)
