import Camera
import UltrasonicModuleControl
import PressureSensor
import MagnetManager
import Accelerometer
import Motor
import ObjectDetector
import Speaker
import StairDetector
import Winch
import time
import logging


class Robot:
    name = None
    motor_wheels = None
    ultrasonic_module_control = None
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
        logging.info("create new Robot")
        self.name = name
        self.motor_wheels = Motor.Motor()
        self.motor_wheels.enable()
        self.ultrasonic_module_control = UltrasonicModuleControl.UltrasonicModuleControl()
        # self.ultrasonic_module_control.calibrate_sensors(distance_sensor_to_object=10) # TODO: Do we have to calibrate after each start?
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
        logging.info("Robot: stop")
        self.motor_wheels.stop()

    def go_forward_slow(self):
        logging.info("Robot: go forward slow")
        self.motor_wheels.rotate(20, 20)

    def go_forward_medium(self):
        logging.info("Robot: go forward medium")
        self.motor_wheels.rotate(50, 50)

    def go_forward_fast(self):
        logging.info("Robot: go forward fast")
        self.motor_wheels.rotate(70, 70)

    def go_backward_slow(self):
        logging.info("Robot: go backward slow")
        self.motor_wheels.rotate(-20, -20)

    def go_backward_medium(self):
        logging.info("Robot: go backward medium")
        self.motor_wheels.rotate(-50, -50)

    def go_backward_fast(self):
        logging.info("Robot: go backward fast")
        self.motor_wheels.rotate(-70, -70)

    def turn_right(self):
        logging.info("Robot: turn right")
        self.motor_wheels.rotate(-30, 30)

    def turn_left(self):
        logging.info("Robot: turn left")
        self.motor_wheels.rotate(30, -30)

    def turn_right_90degrees(self):
        logging.info("Robot: turn right 90 degrees")
        self.turn_right()
        duration_milliseconds = 3000  # TODO: define the correct duration
        time.sleep(duration_milliseconds / 1000)
        self.stop()

    def turn_left_90degrees(self):
        logging.info("Robot: turn right 90 degrees")
        self.turn_left()
        duration_milliseconds = 3000  # TODO: define the correct duration
        time.sleep(duration_milliseconds / 1000)
        self.stop()

    def turn_cam_ahead(self):
        logging.info("Robot: camera turn ahead")
        self.camera.cam_servo.turn_ahead()

    def turn_cam_up(self):
        logging.info("Robot: camera turn up")
        self.camera.cam_servo.turn_up()

    def turn_cam_left(self):
        logging.info("Robot: camera turn down")
        self.camera.cam_servo.turn_down()

    def acknowledge_pictogram(self, found_pictogram_english_lowercase):
        logging.info("Robot: acknowledge pictogram")
        self.speaker.play_text(found_pictogram_english_lowercase)

    def pull_up(self):
        logging.info("Robot: winch pull up")
        self.winch.pull_up(80)  # TODO: define speed

    def let_socket_down(self):
        logging.info("Robot: let socket down")
        self.magnet_manager.set_off_power_socket()

    def let_bridge_down(self):
        logging.info("Robot: let bridge down")
        self.magnet_manager.set_off_power_bridge()

    def celebrate(self, found_pictogram_english_lowercase):
        logging.info("Robot: celebrate")
        self.speaker.celebrate(found_pictogram_english_lowercase)

    def measure_distance_sensor_front(self):
        logging.info("Robot: measure distance sensor front")
        distance = self.ultrasonic_module_control.sensor_front.get_distance_multiple_in_cm()
        return distance

    def measure_distance_sensor_side(self):
        logging.info("Robot: measure distance sensor side")
        distance = self.ultrasonic_module_control.sensor_side.get_distance_multiple_in_cm()
        return distance

    # Below: combined methods

    def turn_and_find_pictogram(self, is_turn_direction_left):
        logging.info("Robot: turn and find pictogram")
        if is_turn_direction_left:
            self.turn_left()
        else:
            self.turn_right()
        is_found, self.found_pictogram = self.object_detector.find_pictogram_start_platform(self.camera.capture)
        self.stop()
        if is_found and self.found_pictogram is not None:
            logging.info("Robot: got target, it is - " + self.found_pictogram)
        else:
            logging.warning("pictogram couldn't be found")
            #  TODO: Define what to do if not is found

    def turn_and_find_stair(self, is_turn_direction_left):
        logging.info("Robot: turn and find stair")
        if is_turn_direction_left:
            self.turn_left()
        else:
            self.turn_right()
        self.stair_detector.find_stair(self.camera.capture)
        duration_eliminate_offset = 200  # TODO: Define duration
        time.sleep(duration_eliminate_offset / 1000)
        self.stop()

    def go_forward_and_get_distance(self):
        logging.info("Robot: go forward and get distance")
        self.go_forward_medium()
        distance = self.ultrasonic_module_control.sensor_front.get_distance_multiple_in_cm()
        offset_to_slow_down_millimeter = 20000  # TODO: Define offset
        while distance > offset_to_slow_down_millimeter:
            distance = self.ultrasonic_module_control.sensor_front.get_distance_multiple_in_cm()
        self.stop()






