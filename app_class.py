# Contains core Seat class definition and related utilities

import random
import string


def generate_random_string(length=8):
    """Generates a random alphanumeric string of specified length"""
    characters = string.ascii_letters + string.digits  # All ASCII letters and digits
    return ''.join(random.choices(characters, k=length))  # Random selection


class Seat:
    """Represents a seat object with booking-related properties and methods"""

    def __init__(self, number):
        """Initialize seat with unique identifier and default values"""
        self.number = number  # Seat identifier (e.g., "12A")
        self.status = 0  # 0=Available, 1=Occupied, 2=Booked (unused in current implementation)
        self.reference_number = generate_random_string()  # Unique booking reference
        self.passport_number = ""  # Passenger identification
        self.first_name = ""  # Passenger details
        self.last_name = ""

    def __str__(self):
        """String representation of the seat (returns seat number)"""
        return str(self.number)

    # Status management methods
    def turn_available(self):
        """Mark seat as available if not already available"""
        if self.status != 0:
            self.status = 0

    def turn_occupied(self):
        """Mark seat as occupied if not already occupied"""
        if self.status != 1:
            self.status = 1

    def turn_booked(self):
        """Mark seat as booked if not already booked (unused in current implementation)"""
        if self.status != 2:
            self.status = 2

    # Passenger information setters
    def set_passport_number(self, passport_number):
        """Store passenger's passport number"""
        self.passport_number = passport_number

    def set_first_name(self, first_name):
        """Store passenger's first name"""
        self.first_name = first_name

    def set_last_name(self, last_name):
        """Store passenger's last name"""
        self.last_name = last_name

    def information_clear(self):
        """Clear all passenger information from seat"""
        self.passport_number = ""
        self.first_name = ""
        self.last_name = ""