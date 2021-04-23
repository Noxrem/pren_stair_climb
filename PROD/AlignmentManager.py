import logging

import UARTAccess


class AlignmentManager:
    cmd_start = "aln start"
    cmd_abort = "aln stop"
    cmd_response = "Alignment completed"
    Button = None
    serial_access = None

    def __init__(self):
        logging.info("init alignmentManager")
        self.serial_access = UARTAccess.UARTAccess()

    def do_alignment(self):
        try:
            response = self.serial_access.write_and_read(self.cmd_start)
            while response != self.cmd_response:
                logging.debug(response)
                logging.debug("pull, pull, pull, pull")
            logging.info("pulled up")
        except Exception:
            self.serial_access.write(self.cmd_abort)
        return
