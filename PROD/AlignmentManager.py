import logging

import UARTAccess


class AlignmentManager:
    cmd_start = "aln start"
    cmd_speed = "aln setSpd"
    cmd_abort = "aln stop"
    cmd_response = "Alignment completed"
    Button = None
    serial_access = None

    def __init__(self):
        logging.info("init alignmentManager")
        self.serial_access = UARTAccess.UARTAccess()

    def do_alignment(self, speed=30):
        try:
            logging.debug("get in dance mood and seek out the juicy stair, send start command")
            self.serial_access.write(self.cmd_start)
            logging.debug("hurrrrrrry, go faster!!!! (or slower)")
            response = self.serial_access.write_and_read(self.cmd_speed+str(speed))
            while response != self.cmd_response:
                logging.debug(response)
                logging.debug("aaaaaaaaa")
                logging.debug("lllllllll")
                logging.debug("iiiiiiiii")
                logging.debug("ggggggggg")
                logging.debug("nnnnnnnnn")
                logging.debug("mmmmmmmmm")
                logging.debug("eeeeeeeee")
                logging.debug("nnnnnnnnn")
                logging.debug("ttttttttt")
            logging.info("lick on your step")
        except Exception:
            logging.error("an error occurred:")
            logging.error(str(Exception))
            self.serial_access.write(self.cmd_abort)
        return
