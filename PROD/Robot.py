import AlignmentManager
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
import StairDetectorWithUltrasonic
import ArmServo


def calculate_duration_length_in_mm(speed, length_target_in_mm):
    duration_in_sec = length_target_in_mm / speed
    return duration_in_sec


def calculate_duration_length_in_cm(speed, length_target_in_cm):
    duration_in_sec = length_target_in_cm * 10 / speed
    return duration_in_sec


class Robot:

    def __init__(self, name):
        logging.info("create new Robot")
        self.name = name
        self.motor_wheels = Motor.Motor()
        self.motor_wheels.enable()  # all motors incl. winch will set to ready state
        self.ultrasonic_module_control = UltrasonicModuleControl.UltrasonicModuleControl()
        # self.ultrasonic_module_control.calibrate_sensors(distance_sensor_to_object=10) # We don't need to calibrate before the start
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
        self.stair_detector_with_ultrasonic = StairDetectorWithUltrasonic.StairDetectorWithUltrasonic()
        self.alignmentManager = AlignmentManager.AlignmentManager()
        self.arm_servo = ArmServo.ArmServo()
        self.target_platform = TargetPlatform.TargetPlatform()
        self.distance_front = None
        self.distance_right = None
        self.found_pictogram = None

    def stop(self):
        logging.info("Robot: stop")
        self.motor_wheels.stop()

    def stop_soft(self, speed):
        logging.info("Robot: stop soft")
        actual_speed = speed
        percent_10_speed = int(speed/10)
        for i in range(9):
            actual_speed = actual_speed - percent_10_speed
            self.motor_wheels.rotate(actual_speed, actual_speed)
            time.sleep(0.1)
        self.stop()

    def go_forward_and_stop_after_duration(self, speed, duration):
        logging.info("Robot: go forward with speed " + str(speed) + " during " + str(duration) + "seconds")
        self.motor_wheels.rotate(speed, speed)
        time.sleep(duration)
        self.stop_soft(speed)

    def go_forward_slow(self):
        logging.info("Robot: go forward slow")
        self.motor_wheels.rotate(30, 30)

    def go_forward_medium(self):
        logging.info("Robot: go forward medium")
        self.motor_wheels.rotate(80, 80)

    def go_forward_fast(self):
        logging.info("Robot: go forward fast")
        self.motor_wheels.rotate(200, 200)

    def go_backward_and_stop_after_duration(self, speed, duration):
        logging.info("Robot: go backwards with speed " + str(speed) + " during " + str(duration) + " seconds")
        self.motor_wheels.rotate(-speed, -speed)
        time.sleep(duration)
        self.stop()

    def go_backward_slow(self):
        logging.info("Robot: go backward slow")
        self.motor_wheels.rotate(-30, -30)

    def go_backward_medium(self):
        logging.info("Robot: go backward medium")
        self.motor_wheels.rotate(-80, -80)

    def go_backward_fast(self):
        logging.info("Robot: go backward fast")
        self.motor_wheels.rotate(-200, -200)

    def turn_right(self, speed=30):
        logging.info("Robot: turn right")
        self.motor_wheels.rotate(-speed, speed)

    def turn_left(self, speed=30):
        logging.info("Robot: turn left")
        self.motor_wheels.rotate(speed, -speed)

    def turn_right_90degrees(self):
        logging.info("Robot: turn right 90 degrees")
        self.motor_wheels.rotate(-50, 50)
        duration_milliseconds = 5500  # TODO: define the correct duration
        time.sleep(duration_milliseconds / 1000)
        self.stop()

    def turn_left_90degrees(self):
        logging.info("Robot: turn left 90 degrees")
        self.motor_wheels.rotate(50, -50)
        duration_milliseconds = 5500  # TODO: define the correct duration
        time.sleep(duration_milliseconds / 1000)
        self.stop()

    def turn_cam_ahead(self):
        logging.info("Robot: camera turn ahead")
        self.camera.cam_servo.turn_ahead()

    def turn_cam_up(self):
        logging.info("Robot: camera turn up")
        self.camera.cam_servo.turn_up()

    def turn_cam_down(self):
        logging.info("Robot: camera turn down")
        self.camera.cam_servo.turn_down()

    def turn_arm_down(self):
        logging.info("Robot: turn arm down")
        self.arm_servo.turn_down()

    def turn_arm_up(self):
        logging.info("Robot: turn arm up")
        self.arm_servo.turn_up()

    def acknowledge_pictogram(self, found_pictogram_english_lowercase):
        logging.info("Robot: acknowledge pictogram")
        self.speaker.play_text(found_pictogram_english_lowercase)

    def pull_up(self):
        logging.info("Robot: winch pull up")
        self.winch.pull_up(70)  # TODO: define speed

    def pull_to_bridge_drop_off(self):
        logging.info("Robot: can see light at the end of the tunnel")
        speed_wheels = 100
        speed_winch = 70
        distance_in_mm_wheels = 100
        distance_in_mm_winch = 175
        duration_wheels = calculate_duration_length_in_mm(speed_wheels, distance_in_mm_wheels)  # todo: define distance and speed
        duration_winch = calculate_duration_length_in_mm(speed_winch, distance_in_mm_winch)  # todo: define distance and speed
        self.winch.pull_to_end(speed_winch, duration_winch)
        self.go_forward_and_stop_after_duration(speed_wheels, duration_wheels)

    def let_socket_down(self):
        logging.info("Robot: let socket down")
        self.magnet_manager.set_off_power_socket()

    def let_bridge_down(self):
        logging.info("Robot: let bridge down")
        # self.speaker.play("getready.mp3", True)  # todo: enable on the competition
        self.magnet_manager.set_off_power_bridge()

    def celebrate(self, found_pictogram_english_lowercase, lap_duration):
        logging.info("Robot: celebrate")
        self.speaker.stop_play()    # stop the previously running music
        self.speaker.celebrate(found_pictogram_english_lowercase, lap_duration)

    def measure_distance_sensor_front(self):
        logging.info("Robot: measure distance sensor front")
        distance = self.ultrasonic_module_control.get_distance_in_cm(0)
        return distance

    def measure_distance_sensor_side(self):
        logging.info("Robot: measure distance sensor side")
        distance = self.ultrasonic_module_control.get_distance_in_cm(1)
        return distance

    def do_alignment(self):
        logging.info("Robot: aligning")
        self.alignmentManager.do_alignment(30)

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
            self.turn_and_find_pictogram(True)

    def turn_and_find_stair_with_ultrasonic_and_camera_control(self, is_running_on_a_display):
        logging.info("Robot: turn and find stair with ultrasonic and camera control")
        self._turn_and_find_stair_only_with_ultrasonic()
        is_stair_found_with_camera = self._find_stair_with_camera(is_running_on_a_display, True)
        if not is_stair_found_with_camera:
            self._turn_and_find_stair_only_with_ultrasonic()

    def turn_and_find_stair_with_camera_and_ultrasonic_control(self):
        logging.info("Robot: turn and find stair with camera and ultrasonic control")
        is_stair_found = False
        self.turn_left()
        while not is_stair_found:
            is_stair_found = self._find_stair_with_camera(True, False)
        self.stop()

    def _find_stair_with_camera(self, is_running_on_a_display, is_running_in_control_mode):
        is_stair_found = False
        logging.info("Robot: find stair with camera")
        self.camera.cam_servo.turn_to_degree(90)
        is_found_with_camera, is_timer_down = self.stair_detector.find_stair(self.camera.capture,
                                                                             is_running_on_a_display,
                                                                             is_running_in_control_mode)  # 2. parameter -> switch on/off display mode
        if is_found_with_camera:
            logging.info("camera has seen something which seems to be a stair. Make a control with distance sensor")
            distance = self.measure_distance_sensor_front()
            if distance < 190:
                logging.info("distance: " + str(distance))
                logging.info("stair is found for sure")
                is_stair_found = True
            else:
                logging.info("it was not the stair")
        else:
            logging.info("stair could not be found.")
        return is_stair_found

    def _turn_and_find_stair_only_with_ultrasonic(self):
        logging.info("Robot: turn and find stair only with ultrasonic")
        self.turn_left()
        min_target_amount = self.stair_detector_with_ultrasonic.find_stair_with_ultrasonic_v2()  # TODO: decide which method should be used
        self.stop()
        logging.info("stair found with ultrasonic")
        self.turn_right()
        time.sleep(min_target_amount * 0.28 / 3)
        self.stop()

    def go_forward_and_get_distance(self):
        logging.info("Robot: go forward and get distance")
        self.go_forward_fast()
        self.distance_front = self.measure_distance_sensor_front()
        offset_to_slow_down_cm = 35  # TODO: Define offset
        while self.distance_front > offset_to_slow_down_cm:
            self.distance_front = self.measure_distance_sensor_front()
            logging.info("\nMeasured Distance = %.2f cm" % self.distance_front)
        self.stop_soft()

    def go_to_drop_off_position(self):
        position_found_pictogram = None
        logging.info("Robot: go forward to drop off position")
        offset_inaccuracy_allowed_max = 2  # TODO: Define value
        offset_sensor_right_and_center_robot = 11.4
        if self.found_pictogram is not None:
            for i in range(len(self.target_platform.list_pictograms)):
                if self.target_platform.list_pictograms.__getitem__(i).name == self.found_pictogram:
                    position_found_pictogram = self.target_platform.list_pictograms.__getitem__(i).position_cm
                    logging.info("The pictogram is on position: " + str(position_found_pictogram))
        else:
            position_found_pictogram = 65  # default value in the middle of the stair
            logging.info("We will use the path in the middle of the stair because we could not find the pictogram")
        self.distance_right = self.measure_distance_sensor_side()
        logging.debug("Distance right: " + str(self.distance_right))
        speed = 50  # TODO: define speed
        target_distance_from_stair = 50  # TODO: define value -> Scharnier der Brücke sollte 60cm von Stufe entfernt sein
        duration_in_sec = calculate_duration_length_in_cm(speed, target_distance_from_stair)
        self.go_backward_and_stop_after_duration(speed, duration_in_sec)
        robot_position = self.distance_right + offset_sensor_right_and_center_robot
        logging.debug("Robot position before move sideways: " + str(robot_position))
        distance_move_sideways = abs(robot_position - position_found_pictogram)
        logging.debug("Distance move sideways: " + str(distance_move_sideways))
        duration_in_sec = calculate_duration_length_in_cm(speed, distance_move_sideways)
        if robot_position - offset_inaccuracy_allowed_max > position_found_pictogram:
            self.turn_right_90degrees()
            logging.debug("Go to the right: " + str(speed * duration_in_sec) + "mm")
            self.speaker.play("getready.mp3", True)
            self.go_forward_and_stop_after_duration(speed, duration_in_sec)
            self.turn_left_90degrees()
        elif robot_position + offset_inaccuracy_allowed_max < position_found_pictogram:
            self.turn_left_90degrees()
            logging.debug("Go to the left: " + str(speed * duration_in_sec) + "mm")
            self.speaker.play("getready.mp3", True)
            self.go_forward_and_stop_after_duration(speed, duration_in_sec)
            self.turn_right_90degrees()
        else:
            logging.info(
                "Distance move sideways is smaller than defined offset_inaccuracy_allowed_max. No move sideways needed")
        logging.info("Robot is on drop off position")

    def dispose(self):
        self.let_bridge_down()  # TODO: Only for test runs to save power
        self.let_socket_down()
        self.stop()
        self.motor_wheels.disable()
        self.turn_arm_up()
