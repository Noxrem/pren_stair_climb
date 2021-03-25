import Robot


class Game:
    robot = Robot.Robot("Gefyra")
    distance_to_stair = None
    is_pictogram_detected = None
    is_stair_detected = None

    def __init__(self):
        print("create new game")
        self.robot = Robot.Robot()
        self.is_pictogram_detected = False
        self.is_stair_detected = False

