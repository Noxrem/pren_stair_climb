from gtts import gTTS
from playsound import playsound


class Speaker:
    texts = None
    celebration_sound = None

    def __init__(self):
        self.texts = ["This is a hammer",
                      "This is a sandwich",
                      "This is a ruler",
                      "This is a paint bucket",
                      "This is a pencil",
                      "This is a wrench"]
        self.celebration_sound = "celebration.mp3"

    def play_text(self, found_pictogram_english_lowercase):
        message = None
        if found_pictogram_english_lowercase == "hammer":
            message = self.texts[0]
        elif found_pictogram_english_lowercase == "sandwich":
            message = self.texts[1]
        elif found_pictogram_english_lowercase == "ruler":
            message = self.texts[2]
        elif found_pictogram_english_lowercase == "paint bucket":
            message = self.texts[3]
        elif found_pictogram_english_lowercase == "pencil":
            message = self.texts[4]
        elif found_pictogram_english_lowercase == "wrench":
            message = self.texts[5]
        language = 'en'
        slow = False
        print("Create MP3 files")
        tts = gTTS(text=message, lang=language, slow=slow)
        tts.save('TTS_message_pictogram.mp3')
        print("Play MP3 files")
        playsound('TTS_message_pictogram.mp3')

    def celebrate(self, found_pictogram_english_lowercase):
        print("Play MP3 files")
        message = "We have found the " + found_pictogram_english_lowercase + ". Gefyra is an amazing Robot."
        language = 'en'
        slow = False
        tts = gTTS(text=message, lang=language, slow=slow)
        tts.save('TTS_message_celebrate.mp3')
        print("Play MP3 files")
        playsound('TTS_message_celebrate.mp3')
        playsound(self.celebration_sound)

