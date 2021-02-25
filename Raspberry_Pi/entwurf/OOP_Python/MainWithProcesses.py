import Robot
import multiprocessing as mp
import time

is_found_pictogram = False
is_found_stair = False
found_pictogram = None
distance_left = None
distance_right = None

robot = Robot.Robot("Gefyra")

NUM_PROCESSES = 4


def task_thread1():
    counter1 = 0
    while counter1 < 100:
        print("Hello from " + str(mp.Process.name) + " from Task1")
        counter1 += 1


with mp.Pool(processes=NUM_PROCESSES) as pool:
    name = mp.Process.name
    print(name)
    task_thread1()
