# pip install playsound
# pip3 install gtts

from gtts import gTTS
from playsound import playsound 

language = 'de'
slow = False
print("Create MP3 files ...")
tts = gTTS(text='Das Piktogramm zeigt einen Hammer', lang=language, slow=slow)
tts.save('TTS_Hammer.mp3')

tts = gTTS(text='Das Piktogramm zeigt einen Kübel', lang=language, slow=slow)
tts.save('TTS_Kuebel.mp3')

print("Play MP3 files ...")
playsound('TTS_Hammer.mp3')
playsound('TTS_Kuebel.mp3')