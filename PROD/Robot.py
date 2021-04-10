import Camera
import DistanceSensor
import PressureSensor
import MagnetManager
import Accelerometer
import Motor
import ObjectDetector
import Speaker
import StairDetector
import Winch
import time


class Robot:
    name = None
    motor_wheels = None
    distance_sensor_front = None
    distance_sensor_side = None
    pressure_sensor_left = None
    pressure_sensor_right = None
    accelerometer = None
    camera = None
    winch = None
    speaker = None
    object_detector = None
    magnet_manager = None
    stair_detector = None
    found_object = None

    def __init__(self, name):
        print("create new Robot")
        self.name = name
        self.motor_wheels = Motor.Motor()
        self.motor_wheels.enable()
        self.distance_sensor_front = DistanceSensor.DistanceSensor()
        self.distance_sensor_side = DistanceSensor.DistanceSensor()
        self.pressure_sensor_left = PressureSensor.PressureSensor()
        self.pressure_sensor_right = PressureSensor.PressureSensor()
        self.accelerometer = Accelerometer.Accelerometer()
        self.camera = Camera.Camera()
        self.winch = Winch.Winch()
        self.speaker = Speaker.Speaker()
        self.object_detector = ObjectDetector.ObjectDetector()
        self.magnet_manager = MagnetManager.MagnetManager()
        self.magnet_manager.set_on_power_bridge()
        self.magnet_manager.set_on_power_socket()
        self.stair_detector = StairDetector.StairDetector()

    def stop(self):
        print("Robot: stop")
        self.motor_wheels.stop()

    def go_forward_slow(self):
        print("Robot: go forward slow")
        self.motor_wheels.rotate(20, 20)

    def go_forward_medium(self):
        print("Robot: go forward medium")
        self.motor_wheels.rotate(50, 50)

    def go_forward_fast(self):
        print("Robot: go forward fast")
        self.motor_wheels.rotate(70, 70)

    def go_backward_slow(self):
        print("Robot: go backward slow")
        self.motor_wheels.rotate(-20, -20)

    def go_backward_medium(self):
        print("Robot: go backward medium")
        self.motor_wheels.rotate(-50, -50)

    def go_backward_fast(self):
        print("Robot: go backward fast")
        self.motor_wheels.rotate(-70, -70)

    def turn_right(self):
        print("Robot: turn right")
        self.motor_wheels.rotate(-30, 30)

    def turn_left(self):
        print("Robot: turn left")
        self.motor_wheels.rotate(30, -30)

    def turn_right_90degrees(self):
        print("Robot: turn right 90 degrees")
        self.turn_right()
        duration_milliseconds = 3000  # TODO: define the correct duration
        time.sleep(duration_milliseconds / 1000)
        self.stop()

    def turn_left_90degrees(self):
        print("Robot: turn right 90 degrees")
        self.turn_left()
        duration_milliseconds = 3000  # TODO: define the correct duration
        time.sleep(duration_milliseconds / 1000)
        self.stop()

    def turn_cam_ahead(self):
        print("Robot: camera turn ahead")
        self.camera.cam_servo.turn_ahead()

    def turn_cam_right(self):
        print("Robot: camera turn right")
        self.camera.cam_servo.turn_right()

    def turn_cam_left(self):
        print("Robot: camera turn left")
        self.camera.cam_servo.turn_left()

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
        distance = self.distance_sensor_front.get_distance_multiple()
        return distance

    def measure_distance_single(self):
        print("Robot: measure distance single")
        distance = self.distance_sensor_front.get_distance_single()
        return distance

    # Below: combined methods

    def turn_and_find_pictogram(self, is_turn_direction_left):
        print("Robot: turn and find pictogram")
        if is_turn_direction_left:
            self.turn_left()
        else:
            self.turn_right()
        is_found, self.found_pictogram = self.object_detector.find_pictogram_start_platform(self.camera.capture)
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
        self.stair_detector.find_stair(self.camera.capture)
        duration_eliminate_offset = 200  # TODO: Define duration
        time.sleep(duration_eliminate_offset / 1000)
        self.stop()

    def go_forward_and_get_distance(self):
        print("Robot: go forward and get distance")
        self.go_forward_medium()
        distance = self.measure_distance_multiple()
        offset_to_slow_down_millimeter = 20000  # TODO: Define offset
        while distance > offset_to_slow_down_millimeter:
            distance = self.measure_distance_multiple()
        self.stop()





