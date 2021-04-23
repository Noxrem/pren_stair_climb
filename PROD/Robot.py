import Camera
import UltrasonicModuleControl
import PressureSensor
import MagnetManager
import Motor
import ObjectDetector
import Speaker
import StairDetector
import Winch
import time
import logging
import TargetPlatform
import UARTAccess


def _calculate_duration(speed, length_target_in_mm):
    duration_in_sec = length_target_in_mm/speed
    return duration_in_sec


class Robot:

    def __init__(self, name):
        logging.info("create new Robot")
        self.name = name
        self.motor_wheels = Motor.Motor()
        self.motor_wheels.enable()
        self.ultrasonic_module_control = UltrasonicModuleControl.UltrasonicModuleControl()
        #self.ultrasonic_module_control.calibrate_sensors(distance_sensor_to_object=10) # TODO: Do we have to calibrate after each start?
        self.pressure_sensor_left = PressureSensor.PressureSensor()
        self.pressure_sensor_right = PressureSensor.PressureSensor()
        self.camera = Camera.Camera()
        self.winch = Winch.Winch()
        self.speaker = Speaker.Speaker()
        self.object_detector = ObjectDetector.ObjectDetector()
        self.magnet_manager = MagnetManager.MagnetManager()
        self.magnet_manager.set_on_power_bridge()
        self.magnet_manager.set_on_power_socket()
        self.stair_detector = StairDetector.StairDetector()
        self.target_platform = TargetPlatform.TargetPlatform()
        self.distance_front = None
        self.distance_right = None

    def stop(self):
        logging.info("Robot: stop")
        self.motor_wheels.stop()

    def go_forward_and_stop_after_duration(self, speed, duration):
        logging.info("Robot: go forward with speed " + str(speed) + " mm during " + str(duration) + "seconds")
        self.motor_wheels.rotate(speed, speed)
        time.sleep(duration)
        self.stop()

    def go_forward_slow(self):
        logging.info("Robot: go forward slow")
        self.motor_wheels.rotate(20, 20)

    def go_forward_medium(self):
        logging.info("Robot: go forward medium")
        self.motor_wheels.rotate(50, 50)

    def go_forward_fast(self):
        logging.info("Robot: go forward fast")
        self.motor_wheels.rotate(70, 70)

    def go_backward_and_stop_after_duration(self, speed, duration):
        logging.info("Robot: go backwards with speed " + str(speed) + " mm during " + str(duration) + " seconds")
        self.motor_wheels.rotate(-speed, -speed)
        time.sleep(duration)
        self.stop()

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
        time.sleep(duration_milliseconds / 1000 - UARTAccess.timeout_to_read)
        self.stop()

    def turn_left_90degrees(self):
        logging.info("Robot: turn left 90 degrees")
        self.turn_left()
        duration_milliseconds = 3000  # TODO: define the correct duration
        time.sleep(duration_milliseconds / 1000 - UARTAccess.timeout_to_read)
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
        self.winch.pull_up(70)  # TODO: define speed

    def let_socket_down(self):
        logging.info("Robot: let socket down")
        self.magnet_manager.set_off_power_socket()

    def let_bridge_down(self):
        logging.info("Robot: let bridge down")
        self.speaker.play("getready.mp3", True)
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
        self.stair_detector.find_stair(self.camera.capture, False)  # 2. parameter -> switch on/off display mode
        duration_eliminate_offset = 200  # TODO: Define duration
        time.sleep(duration_eliminate_offset / 1000)
        self.stop()

    def go_forward_and_get_distance(self):
        logging.info("Robot: go forward and get distance")
        self.go_forward_medium()
        self.distance_front = self.ultrasonic_module_control.sensor_front.get_distance_multiple_in_cm()
        offset_to_slow_down_millimeter = 20000  # TODO: Define offset
        while self.distance_front > offset_to_slow_down_millimeter:
            self.distance_front = self.ultrasonic_module_control.sensor_front.get_distance_multiple_in_cm()
        self.stop()

    def get_distance_side(self):
        self.distance_right = self.ultrasonic_module_control.sensor_side.get_distance_multiple_in_cm()

    def go_to_drop_off_position(self):
        logging.info("Robot: go forward to drop off position")
        self.found_pictogram = "hammer"  # TODO: Remove this line
        offset_inaccuracy_allowed_max = 20  # TODO: Define value
        offset_sensor_right_and_center_robot = 114
        position_found_pictogram = 650  # default value in the middle of the stair
        for i in range(len(self.target_platform.list_pictograms)):
            if self.target_platform.list_pictograms.__getitem__(i).name == self.found_pictogram:
                position_found_pictogram = self.target_platform.list_pictograms.__getitem__(i).position_mm
                logging.info("The pictogram is on position: " + str(position_found_pictogram))
        #self.get_distance_side()  #  TODO: activate
        self.distance_right = 167  #TODO: remove this line
        logging.debug("Distance right: " + str(self.distance_right))
        speed = 100  # TODO: define speed
        target_distance_from_stair = 500  # TODO: define value -> Scharnier der Brücke sollte 600mm von Stufe entfernt sein
        duration_in_sec = _calculate_duration(speed, target_distance_from_stair)
        self.go_backward_and_stop_after_duration(speed, duration_in_sec)
        robot_position = self.distance_right + offset_sensor_right_and_center_robot
        logging.debug("Robot position before move sideways: " + str(robot_position))
        distance_move_sideways = abs(robot_position - position_found_pictogram)
        logging.debug("Distance move sideways: " + str(distance_move_sideways))
        duration_in_sec = _calculate_duration(speed, distance_move_sideways)
        if robot_position - offset_inaccuracy_allowed_max > position_found_pictogram:
            self.turn_right_90degrees()
            logging.debug("Go to the right: " + str(speed*duration_in_sec) + "mm")
            self.go_forward_and_stop_after_duration(speed, duration_in_sec)
            self.turn_left_90degrees()
        elif robot_position + offset_inaccuracy_allowed_max < position_found_pictogram:
            self.turn_left_90degrees()
            logging.debug("Go to the left: " + str(speed*duration_in_sec) + "mm")
            self.go_forward_and_stop_after_duration(speed, duration_in_sec)
            self.turn_right_90degrees()
        else:
            logging.info("Distance move sideways is smaller than defined offset_inaccuracy_allowed_max. No move sideways needed")
        logging.info("Robot is on drop off position")


