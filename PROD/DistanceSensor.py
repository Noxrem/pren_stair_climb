class DistanceSensor:
    amount_of_multiple_measurements = 5  # TODO: Anzahl Messungen definieren

    def __init__(self):
        print("create new distance sensor")

    def get_distance_single(self):
        print("get distance single")
        distance = DistanceSensor._receive_distance(self)
        return distance

    def get_distance_multiple(self):
        print("get distance multiple")
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
        # TODO: Nathi: Implementation
        distance = 0
        print("Distance: " + str(distance))
        return distance
