import logging
import Motor
import UARTAccess


class AlignmentManager:
    cmd_start = "aln start"
    cmd_speed = "aln setSpd "   # With an appended SPACE char
    cmd_abort = "aln stop"
    cmd_start_response = "Alignment started\n"
    cmd_response = "Alignment completed\n"
    Button = None
    serial_access = None

    def __init__(self):
        logging.info("init alignmentManager")
        self.serial_access = UARTAccess.UARTAccess()
        self.motor = Motor.Motor()   # intitialize motor

    def do_alignment(self, speed=30):
        self.motor.enable()
        try:
            logging.debug("set alignment speed to " + str(speed) + "mm/s")
            self.serial_access.write(self.cmd_speed + str(speed))   # Set the speed of the alignment process
            logging.debug("get in dance mood and seek out the juicy stair, send start command")
            response = self.serial_access.write_and_read(self.cmd_start)
            #if response != str.encode(self.cmd_start_response):                # Raise Exception if no start acknowledge received
            #   raise ValueError("Alignment not started!")
            # TODO next line runns endlessly
            while self.serial_access.read() != str.encode(self.cmd_response):   # Wait for alignment to finish
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
        except Exception as e:
            logging.error("an error occurred:")
            logging.error(str(e))
            self.serial_access.write(self.cmd_abort)
        return
