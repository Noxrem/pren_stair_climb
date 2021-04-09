from gtts import gTTS
from playsound import playsound


class Speaker:
    texts = None
    celebration_sound = None
    language = None

    def __init__(self):
        print("create new speaker")
        self.texts = ["This is a hammer",
                      "This is a sandwich",
                      "This is a ruler",
                      "This is a paint bucket",
                      "This is a pencil",
                      "This is a wrench"]
        self.celebration_sound = "celebration.mp3"
        self.language = 'en'

    def play_text(self, found_pictogram_english_lowercase):
        message = None
        if found_pictogram_english_lowercase == "hammer":
            message = self.texts[0]
        elif found_pictogram_english_lowercase == "wrap":
            message = self.texts[1]
        elif found_pictogram_english_lowercase == "ruler":
            message = self.texts[2]
        elif found_pictogram_english_lowercase == "paint bucket":
            message = self.texts[3]
        elif found_pictogram_english_lowercase == "pencil":
            message = self.texts[4]
        elif found_pictogram_english_lowercase == "wrench":
            message = self.texts[5]
        slow = False
        print("Create MP3 file with pictogram text")
        tts = gTTS(text=message, lang=self.language, slow=slow)
        tts.save('TTS_message_pictogram.mp3')
        print("Play MP3 file with pictogram text")
        playsound('TTS_message_pictogram.mp3')

    def celebrate(self, found_pictogram_english_lowercase):
        print("celebrate")
        message = "We have found the " + found_pictogram_english_lowercase
        slow = False
        tts = gTTS(text=message, lang=self.language, slow=slow)
        tts.save('TTS_message_celebrate.mp3')
        print("Play MP3 file celebration")
        playsound('TTS_message_celebrate.mp3')
        playsound(self.celebration_sound)

