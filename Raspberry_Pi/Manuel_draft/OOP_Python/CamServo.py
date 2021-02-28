class CamServo:

    is_ahead = None

    def __init__(self):
        self.is_ahead = True

    def turn_ahead(self):
        if not self.is_ahead:
            print("turn cam servo ahead")
            # TODO: define Interface
            self.is_ahead = True

    def turn_right(self):
        if self.is_ahead:
            print("turn cam servo ahead")
            # TODO: define Interface
            self.is_ahead = False
