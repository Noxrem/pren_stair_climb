import logging


class Pictogram:
    name = None
    position_0_to_4 = None
    position_cm = None

    def __init__(self, text, position_0_to_4):
        logging.debug("create new Pictogram " + str(text))
        self.name = text
        self.position_0_to_4 = position_0_to_4
        self.position_cm = self._set_position_pictograms_in_cm(position_0_to_4)

    def _set_position_pictograms_in_cm(self, position_0_to_4):
        logging.debug("set position pictograms in cm ")
        if position_0_to_4 == 0:
            self.position_cm = 23
        elif position_0_to_4 == 1:
            self.position_cm = 45
        elif position_0_to_4 == 2:
            self.position_cm = 67
        elif position_0_to_4 == 3:
            self.position_cm = 89
        elif position_0_to_4 == 4:
            self.position_cm = 111
        return self.position_cm
