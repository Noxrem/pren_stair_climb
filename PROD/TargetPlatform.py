import Pictogram
import logging


class TargetPlatform:
    pictogram_hammer = None
    pictogram_wrap = None
    pictogram_paint_bucket = None
    pictogram_ruler = None
    pictogram_pencil = None
    pictogram_wrench = None
    list_pictograms = None

    def __init__(self):
        # Info: pictogram with number 5 isn't on the target plattform
        logging.info("create new target plattform")
        self.pictogram_hammer = Pictogram.Pictogram("hammer", 0)
        self.pictogram_wrap = Pictogram.Pictogram("wrap", 1)
        self.pictogram_paint_bucket = Pictogram.Pictogram("paint_bucket", 2)
        self.pictogram_ruler = Pictogram.Pictogram("ruler", 3)
        self.pictogram_pencil = Pictogram.Pictogram("pencil", 4)
        self.pictogram_wrench = Pictogram.Pictogram("wrench", 5)

    def print_pictogram_order(self):
        logging.info("***************print pictogram order****************")
        self.list_pictograms = [self.pictogram_hammer, self.pictogram_wrap,
                                self.pictogram_paint_bucket, self.pictogram_ruler,
                                self.pictogram_pencil, self.pictogram_wrench]
        for i in range(len(self.list_pictograms)-1):
            logging.info(str(self.list_pictograms.__getitem__(i).text) + "/" +
                         str(self.list_pictograms.__getitem__(i).position_0_to_4) + "/" +
                         str(self.list_pictograms.__getitem__(i).position_mm))
