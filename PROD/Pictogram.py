import logging


class Pictogram:
    name = None
    position_0_to_4 = None
    position_mm = None

    def __init__(self, text, position_0_to_4):
        logging.debug("create new Pictogram " + str(text))
        self.name = text
        self.position_0_to_4 = position_0_to_4
        self.position_mm = self._set_position_pictograms_in_mm(position_0_to_4)

    def _set_position_pictograms_in_mm(self, position_0_to_4):
        logging.debug("set position pictograms in mm ")
        if position_0_to_4 == 0:
            self.position_mm = 230
        elif position_0_to_4 == 1:
            self.position_mm = 450
        elif position_0_to_4 == 2:
            self.position_mm = 670
        elif position_0_to_4 == 3:
            self.position_mm = 890
        elif position_0_to_4 == 4:
            self.position_mm = 1110
        return self.position_mm
