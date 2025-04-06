import random
import string

def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

class Seat:
    def __init__(self,number):
        self.number = number
        self.status = 0
        self.reference_number = generate_random_string()


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

    def passport_number(self,passport_number):
        self.passport_number = passport_number

    def first_name(self,first_name):
        self.first_name = first_name

    def last_name(self,last_name):
        self.last_name = last_name


    def information_clear(self):
        self.passport_number = ""
        self.first_name = ""
        self.last_name = ""