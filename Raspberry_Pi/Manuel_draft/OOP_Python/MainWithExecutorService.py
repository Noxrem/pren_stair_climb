import Robot
import concurrent.futures
from threading import Thread
import time

is_found_pictogram = False
is_found_stair = False
found_pictogram = None
distance_left = None
distance_right = None

robot = Robot.Robot("Gefyra")


def turn_during_searching_stair():
    while not is_found_stair:
        robot.turn_right_1degree()
        time.sleep(0.2)


def turn_during_measuring_distance():
    while abs(int(distance_right) - int(distance_left)) > 2:
        robot.turn_right_1degree()
        time.sleep(0.2)


def measure_distance_during_turning():
    # entspricht do-while-Schleife
    while True:
        dist_left, dist_right = robot.measure_distance_multiple()
        print("distance left: " + str(dist_left))
        print("distance right: " + str(dist_right))
        if abs(int(dist_right) - int(dist_left)) <= 2:
            return dist_left, dist_right


# Einlesen Piktorgramm
while not is_found_pictogram:
    is_found_pictogram, found_pictogram = robot.object_detector.find_pictogram()

robot.acknowledge_pictogram(found_pictogram)

# Drehen und Treppe suchen
with concurrent.futures.ThreadPoolExecutor(2) as executor:
    future1 = executor.submit(robot.search_stair)
    executor.submit(turn_during_searching_stair)
    is_found_stair = future1.result()
    print(is_found_stair)

# Drehen und Distanz messen
distance_left, distance_right = robot.measure_distance_multiple()
with concurrent.futures.ThreadPoolExecutor(2) as executor:
    future1 = executor.submit(measure_distance_during_turning)
    executor.submit(turn_during_measuring_distance)
    distance_left, distance_right = future1.result()
    print("distance left: " + str(distance_left))
    print("distance right: " + str(distance_right))

robot.winch.pull_up()
robot.final_celebrate(found_pictogram)
