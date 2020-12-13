# pip3 install pygame
# pip3 install gtts

from gtts import gTTS
from pygame import mixer


print("Start TTS application ...")

print("Create MP3 file ...")
tts = gTTS(text='Das Piktogramm zeigt einen hammer mässigen Hammer', lang='de')
tts.save('TTS_Hammer.mp3')


print("Play MP3 file ...")
mixer.init()
mixer.music.load('TTS_Hammer.mp3')
mixer.music.play()

# Wait to finish when opening from cmd
while mixer.music.get_busy():
    pass