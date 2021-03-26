import Camera
import DistanceSensor
import MagnetManager
import Motor
import ObjectDetector
import Speaker
import StairDetector
import Winch
import time


class Robot:
    name = None
    motor_pair = None
    distance_sensor = None
    winch = None
    speaker = None
    object_detector = None
    magnet_manager = None
    stair_detector = None
    camera = None
    found_object = None
    distance_to_stair = None

    def __init__(self, name):
        print("create new Robot")
        self.name = name
        self.camera = Camera.Camera()
        self.motor_pair = Motor.Motor()
        self.motor_pair.enable()
        self.distance_sensor = DistanceSensor.DistanceSensor()
        self.winch = Winch.Winch()
        self.speaker = Speaker.Speaker()
        self.object_detector = ObjectDetector.ObjectDetector(self.camera)
        self.magnet_manager = MagnetManager.MagnetManager()
        self.magnet_manager.set_on_power_bridge()
        self.magnet_manager.set_on_power_socket()
        self.stair_detector = StairDetector.StairDetector(self.camera)

    def stop(self):
        print("Robot: stop")
        self.motor_pair.stop()

    def go_forward_slow(self):
        print("Robot: go forward slow")
        self.motor_pair.rotate(10, 10)

    def go_forward_medium(self):
        print("Robot: go forward medium")
        self.motor_pair.rotate(30, 30)

    def go_forward_fast(self):
        print("Robot: go forward fast")
        self.motor_pair.rotate(50, 50)

    def go_backward_slow(self):
        print("Robot: go backward slow")
        self.motor_pair.rotate(-10, -10)

    def go_backward_medium(self):
        print("Robot: go backward medium")
        self.motor_pair.rotate(-30, -30)

    def go_backward_fast(self):
        print("Robot: go backward fast")
        self.motor_pair.rotate(-50, -50)

    def turn_right(self):
        print("Robot: turn right")
        self.motor_pair.rotate(-10, 10)

    def turn_left(self):
        print("Robot: turn left")
        self.motor_pair.rotate(10, -10)

    def turn_right_90degrees(self):
        print("Robot: turn right 90 degrees")
        self.turn_right()
        duration_milliseconds = 3000  # TODO: define the correct duration
        time.sleep(duration_milliseconds / 1000)

    def turn_left_90degrees(self):
        print("Robot: turn right 90 degrees")
        self.turn_left()
        duration_milliseconds = 3000  # TODO: define the correct duration
        time.sleep(duration_milliseconds / 1000)

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

    def measure_distance_multiple(self):
        print("Robot: measure distance multiple")
        self.distance = self.distance_sensor.get_distance_multiple()

    def measure_distance_single(self):
        print("Robot: measure distance single")
        self.distance = self.distance_sensor.get_distance_single()

    # Below: combined methods

    def turn_and_find_pictogram(self, is_turn_direction_left):
        print("Robot: turn and find pictogram")
        if is_turn_direction_left:
            self.turn_left()
        else:
            self.turn_right()
        is_found, self.found_pictogram = self.object_detector.find_pictogram_start_platform()
        self.stop()
        if not is_found:
            print("pictogram couldn't be found")
            #  TODO: Define what to do if not is found

    def turn_and_find_stair(self, is_turn_direction_left):
        print("Robot: turn and find stair")
        if is_turn_direction_left:
            self.turn_left()
        else:
            self.turn_right()
        self.stair_detector.find_stair()
        duration_eliminate_offset = 200  # TODO: Define duration
        time.sleep(duration_eliminate_offset / 1000)
        self.stop()

    # Below: private methods




