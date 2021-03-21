class DistanceSensor:
    distance = None
    target_distance_set_down_socket = 30  # TODO: Distanz definieren
    amount_of_multiple_measurements = 5  # TODO: Anzahl Messungen definieren

    def __init__(self):
        self.distance = 15
        print("new distance sensor created")

    def get_available_arguments(self):
        message = "dst help"
        print(message)
        available_arguments = []
        return available_arguments

    def get_distance_single(self):
        message = "dst" + " s"
        print(message)
        self.distance = DistanceSensor.receive_distance(self)
        return self.distance

    def get_distance_multiple(self):
        message = "dst" + " m"
        print(message)
        distances = []
        counter = 0
        sum_distances = 0
        for i in range(self.amount_of_multiple_measurements):
            self.distance = DistanceSensor.receive_distance(self)
            distances.insert(counter, self.distance)
            sum_distances += self.distance
            counter += 1
        self.distance = sum_distances / self.amount_of_multiple_measurements
        return self.distance

    def receive_distance(self):
        # TODO: Distanz über UART empfangen und zuweisen
        print("Distance: " + str(self.distance))
        return self.distance
