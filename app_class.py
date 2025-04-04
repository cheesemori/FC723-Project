"""class Flight:
    def __init__(self,number,departure,destination,departure_time,arrival_time,seats):
        self.number = number
        self.departure = departure
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
"""
class Seat:
    def __init__(self,number):
        self.number = number
        self.status = 0

    def __str__(self):
        return str(self.number)

    def turn_available(self):
        if self.status != 0:
            self.status = 0

    def turn_occupied(self):
        if self.status != 1:
            self.status = 1

    def turn_booked(self):
        if self.status != 2:
            self.status = 2



