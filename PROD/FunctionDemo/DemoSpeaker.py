import Speaker
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


speaker = Speaker.Speaker()
speaker.play_text("hammer")
speaker.celebrate("hammer")

