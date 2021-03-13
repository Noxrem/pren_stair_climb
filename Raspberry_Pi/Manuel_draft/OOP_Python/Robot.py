import Motor
import DistanceSensor
import Winch
import Speaker
import ObjectDetector
import MagnetManager
import StairDetector


class Robot:
    name = None
    motor_left = None
    motor_right = None
    distance_sensor_left = None
    distance_sensor_right = None
    winch = None
    speaker = None
    object_detector = None
    magnet_manager = None
    stair_detector = None

    def __init__(self, name):
        self.name = name
        self.motor_left = Motor.Motor()
        self.motor_right = Motor.Motor()
        self.distance_sensor_left = DistanceSensor.DistanceSensor()
        self.distance_sensor_right = DistanceSensor.DistanceSensor()
        self.winch = Winch.Winch()
        self.speaker = Speaker.Speaker()
        self.object_detector = ObjectDetector.ObjectDetector()
        self.magnet_manager = MagnetManager.MagnetManager()
        self.magnet_manager.set_on_power_bridge()
        self.magnet_manager.set_on_power_socket()
        self.stair_detector = StairDetector.StairDetector()

    # TODO: Momentane Annahme: 1 Grad Drehung bei 30 Millisekunden Rotation

    def go_forward(self):
        self.motor_left.enable()
        self.motor_right.enable()
        self.motor_left.rotate("setL", "50", "30")
        self.motor_right.rotate("setR", "50", "30")

    def go_backward(self):
        self.motor_left.enable()
        self.motor_right.enable()
        self.motor_left.rotate("setL", "-50", "30")
        self.motor_right.rotate("setR", "-50", "30")

    def turn_right_90degrees(self):
        self.motor_left.enable()
        self.motor_right.enable()
        self.motor_left.rotate("setL", "50", "2700")
        self.motor_right.rotate("setR", "-50", "2700")

    def turn_left_90degrees(self):
        self.motor_left.enable()
        self.motor_right.enable()
        self.motor_left.rotate("setL", "-50", "2700")
        self.motor_right.rotate("setR", "50", "2700")

    def turn_left_1degree(self):
        self.motor_left.enable()
        self.motor_right.enable()
        self.motor_left.rotate("setL", "-50", "30")
        self.motor_right.rotate("setR", "50", "30")

    def turn_right_1degree(self):
        self.motor_left.enable()
        self.motor_right.enable()
        self.motor_left.rotate("setL", "-50", "30")
        self.motor_right.rotate("setR", "50", "30")

    def turn_cam_ahead(self):
        self.object_detector.camera.camServo.turn_ahead()

    def turn_cam_right(self):
        self.object_detector.camera.camServo.turn_right()

    def acknowledge_pictogram(self, found_pictogram_english_lowercase):
        self.speaker.play_text(found_pictogram_english_lowercase)

    def pull_up(self):
        self.winch.pull_up()

    def let_socket_down(self):
        self.magnet_manager.set_off_power_socket()

    def let_bridge_down(self):
        self.magnet_manager.set_off_power_bridge()

    def final_celebrate(self, found_pictogram_english_lowercase):
        self.speaker.celebrate(found_pictogram_english_lowercase)

    def search_pictogram(self):
        self.object_detector.find_pictogram()

    def search_stair(self):
        return self.stair_detector.find_stair()

    def measure_distance_multiple(self):
        distance_left = self.distance_sensor_left.get_distance_multiple("left")
        distance_right = self.distance_sensor_right.get_distance_multiple("right")
        return distance_left, distance_right

    def measure_distance_single(self):
        distance_left = self.distance_sensor_left.get_distance_single("left")
        distance_right = self.distance_sensor_right.get_distance_single("right")
        return distance_left, distance_right




