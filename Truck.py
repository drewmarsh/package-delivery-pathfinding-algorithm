class Truck:
    def __init__(self, capacity, speed, load, packages, mileage, address, depart_time, number, is_finished, time_spent):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time
        self.number = number
        self.is_finished = is_finished
        self.time_spent = time_spent

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.load, self.packages, self.mileage,
                                               self.address, self.depart_time)

    def update_mileage(self, distance):
        self.mileage += distance

    def get_number_string(self):
        return f"{self.number}"