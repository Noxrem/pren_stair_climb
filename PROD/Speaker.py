import os
import time

from gtts import gTTS
import logging


class Speaker:
    celebration_sound = None
    language = None

    def __init__(self):
        logging.info("create new speaker")
        self.celebration_sound = "celebration.mp3"
        self.language = 'en'

    def play_text(self, found_pictogram_english_lowercase):
        message = "We can see a " + found_pictogram_english_lowercase + ", will immediately searching it!"
        logging.info("Create MP3 file for pictogram %s", message)
        tts = gTTS(text=message, lang=self.language, slow=False)
        mp3 = 'TTS_message_pictogram.mp3'
        tts.save(mp3)
        self.play(mp3)
        logging.info("Play MP3 file with pictogram text")

    def celebrate(self, found_pictogram_english_lowercase):
        logging.info("!!!!celebrate!!!")
        message = "We have found the target icon " + found_pictogram_english_lowercase
        tts = gTTS(text=message, lang=self.language, slow=False)
        mp3 = "TTS_message_celebrate.mp3"
        tts.save(mp3)
        logging.info("Play MP3 file celebration")
        self.play(mp3)
        logging.info("Party on!!!")
        self.play(self.celebration_sound, True, 20, "No drinks anymore.. so were gonna leave")

    def play(self, path_to_file, play_background=False, duration=None, log_msg=None):
        logging.info("Got file to play: " + path_to_file)
        logging.info("enjoy..")
        if play_background:
            os.system("omxplayer " + path_to_file + " &")
        else:
            os.system("omxplayer " + path_to_file)
        if duration is not None:
            time.sleep(duration)
            logging.info(log_msg)
            os.system("pkill omxplayer")
