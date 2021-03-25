import Camera
import DistanceSensor
import MagnetManager
import Motor
import ObjectDetector
import Speaker
import StairDetector
import Winch


class Robot:
    name = None
    motor_left = None
    motor_right = None
    distance_sensor = None
    winch = None
    speaker = None
    object_detector = None
    magnet_manager = None
    stair_detector = None
    camera = None

    def __init__(self, name):
        print("create new Robot")
        self.name = name
        self.motor_left = Motor.Motor()
        self.motor_right = Motor.Motor()
        self.distance_sensor = DistanceSensor.DistanceSensor()
        self.winch = Winch.Winch()
        self.speaker = Speaker.Speaker()
        self.object_detector = ObjectDetector.ObjectDetector()
        self.magnet_manager = MagnetManager.MagnetManager()
        self.magnet_manager.set_on_power_bridge()
        self.magnet_manager.set_on_power_socket()
        self.stair_detector = StairDetector.StairDetector()
        self.camera = Camera.Camera()

    # TODO: Momentane Annahme: 1 Grad Drehung bei 30 Millisekunden Rotation

    def go_forward(self):
        print("Robot: go forward")
        self.motor_left.enable()
        self.motor_right.enable()
        self.motor_left.rotate("setL", "50", "30")
        self.motor_right.rotate("setR", "50", "30")
        self.motor_left.disable()
        self.motor_right.disable()

    def go_backward(self):
        print("Robot: go backward")
        self.motor_left.enable()
        self.motor_right.enable()
        self.motor_left.rotate("setL", "-50", "30")
        self.motor_right.rotate("setR", "-50", "30")
        self.motor_left.disable()
        self.motor_right.disable()

    def turn_right_90degrees(self):
        print("Robot: turn right 90 degrees")
        self.motor_left.enable()
        self.motor_right.enable()
        self.motor_left.rotate("setL", "50", "2700") # TODO: Is third parameter "duration" needed? Here: 1 degree = 30 milliseconds
        self.motor_right.rotate("setR", "-50", "2700")
        self.motor_left.disable()
        self.motor_right.disable()

    def turn_left_90degrees(self):
        print("Robot: turn left 90 degrees")
        self.motor_left.enable()
        self.motor_right.enable()
        self.motor_left.rotate("setL", "-50", "2700") # TODO: Is third parameter "duration" needed? Here: 1 degree = 30 milliseconds
        self.motor_right.rotate("setR", "50", "2700")
        self.motor_left.disable()
        self.motor_right.disable()

    def turn_right_1degree(self):
        print("Robot: turn right 1 degree")
        self.motor_left.enable()
        self.motor_right.enable()
        self.motor_left.rotate("setL", "50", "30")
        self.motor_right.rotate("setR", "-50", "30")
        self.motor_left.disable()
        self.motor_right.disable()

    def turn_left_1degree(self):
        print("Robot: turn left 1 degree")
        self.motor_left.enable()
        self.motor_right.enable()
        self.motor_left.rotate("setL", "-50", "30")
        self.motor_right.rotate("setR", "50", "30")
        self.motor_left.disable()
        self.motor_right.disable()

    def turn_cam_ahead(self):
        if not self.camera.camServo.is_ahead:
            print("Robot: camera turn ahead")
            self.camera.turn_ahead()
        else:
            print("Robot: camera is already turned ahead")

    def turn_cam_right(self):
        if self.camera.camServo.is_ahead:
            print("Robot: camera turn right")
            self.camera.turn_right()
        else:
            print("Robot: camera is already turned right")

    def acknowledge_pictogram(self, found_pictogram_english_lowercase):
        print("Robot: acknowledge pictogram")
        self.speaker.play_text(found_pictogram_english_lowercase)

    def pull_up(self):
        print("Robot: winch pull up")
        self.winch.pull_up()

    def let_socket_down(self):
        print("Robot: let socket down")
        self.magnet_manager.set_off_power_socket()

    def let_bridge_down(self):
        print("Robot: let bridge down")
        self.magnet_manager.set_off_power_bridge()

    def celebrate(self, found_pictogram_english_lowercase):
        print("Robot: celebrate")
        self.speaker.celebrate(found_pictogram_english_lowercase)

    def find_pictogram(self):
        print("Robot: find pictogram")
        self.object_detector.find_pictogram()

    def find_stair(self):
        print("Robot: find stair")
        return self.stair_detector.find_stair()

    def measure_distance_multiple(self):
        print("Robot: measure distance multiple")
        distance = self.distance_sensor.get_distance_multiple()
        return distance

    def measure_distance_single(self):
        print("Robot: measure distance single")
        distance = self.distance_sensor.get_distance_single()
        return distance




