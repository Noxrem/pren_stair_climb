import random


class DistanceSensor:
    distance = 0

    def __init__(self):
        self.distance = 0
        print("new distance sensor created")

    def get_available_arguments(self):
        command = "dst help"
        print(command)
        available_arguments = []
        return available_arguments

    def get_distance_single(self, side_arg1):
        command = "dst " + side_arg1 + " s"
        print(command)
        self.distance = DistanceSensor.receive_distance(self)
        return self.distance

    def get_distance_multiple(self, side_arg1):
        command = "dst " + side_arg1 + " m"
        print(command)
        self.distance = DistanceSensor.receive_distance(self)
        return self.distance

    def receive_distance(self):
        # TODO: Distanz über UART empfangen und zuweisen
        distance = random.randint(0, 2_000)
        print("Distance: " + str(distance))
        return distance

