class DistanceSensor:
    target_distance_set_down_socket = 30  # TODO: Distanz definieren
    amount_of_multiple_measurements = 5  # TODO: Anzahl Messungen definieren

    def __init__(self):
        print("create new distance sensor")

    def get_available_arguments(self):
        message = "dst help"
        print(message)
        available_arguments = []
        return available_arguments

    def get_distance_single(self):
        message = "dst" + " s"
        print(message)
        distance = DistanceSensor._receive_distance(self)
        return distance

    def get_distance_multiple(self):
        message = "dst" + " m"
        print(message)
        distances = []
        counter = 0
        sum_distances = 0
        for i in range(self.amount_of_multiple_measurements):
            distance = DistanceSensor._receive_distance(self)
            distances.insert(counter, distance)
            sum_distances += distance
            counter += 1
        distance = sum_distances / self.amount_of_multiple_measurements
        return distance

    def _receive_distance(self):
        # TODO: Methode von Nati integrieren
        distance = 0
        print("Distance: " + str(distance))
        return distance
