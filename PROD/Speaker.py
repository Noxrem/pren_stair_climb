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
        message = "We can see the target icon " + found_pictogram_english_lowercase
        logging.info("Create MP3 file for pictogram %s", message)
        tts = gTTS(text=message, lang=self.language, slow=False)
        mp3 = 'TTS_message_pictogram.mp3'
        tts.save(mp3)
        self.play(mp3)
        logging.info("Play MP3 file with pictogram text")

    def celebrate(self, found_pictogram_english_lowercase, lap_duration=20):
        logging.info("!!!!celebrate!!!")
        hour, minutes, seconds = self.convert(round(lap_duration, 2))
        duration_string = str(minutes) + "minutes and " + str(seconds) + "seconds"
        message = "We have found the target icon " + found_pictogram_english_lowercase + "and we need + " + duration_string + " to do so"
        tts = gTTS(text=message, lang=self.language, slow=False)
        mp3 = "TTS_message_celebrate.mp3"
        tts.save(mp3)
        logging.info("Play MP3 file celebration")
        self.play(mp3)
        logging.info("Party on!!!")
        self.play(self.celebration_sound, True, 20, "No drinks anymore.. so were going home then")

    # Convert seconds
    # into hours, minutes and seconds
    def convert(self, seconds):
        minute, sec = divmod(seconds, 60)
        hour, minute = divmod(minute, 60)
        return hour, minute, sec

    @staticmethod
    def play(path_to_file, play_background=False, duration=None, log_msg=None):
        logging.info("Got file to play: " + path_to_file)
        logging.info("enjoy..")
        if play_background:
            os.system("omxplayer " + path_to_file + " &")
        else:
            os.system("omxplayer " + path_to_file)
        # if duration is not None:
        #     time.sleep(duration) # wati until the audio is played
        #     logging.info(log_msg)
        #     Speaker.stop_play()

    @staticmethod
    def stop_play():
        os.system("pkill omxplayer")
