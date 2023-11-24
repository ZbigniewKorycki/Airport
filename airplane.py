from datetime import timedelta
from setup_logging import setup_logging
import random
import numpy as np


class Airplane:
    logger = setup_logging('dev')

    def __init__(self, width=30, length=40, height=10, minutes_of_remaining_fuel=180):
        self.width = width
        self.length = length
        self.height = height
        self.time_of_remaining_fuel = timedelta(minutes=minutes_of_remaining_fuel)
        self.position = self.get_starting_position()
        self.is_landing = False
        self.fuel_reserves_status = "GREEN"

    def get_starting_position(self):
        options = [{"x": 0, "y": random.choice(range(0, 10000))},
                   {"x": 10000, "y": random.choice(range(0, 10000))},
                   {"x": random.choice(range(0, 10000)), "y": 0},
                   {"x": random.choice(range(0, 10000)), "y": 10000}]
        option = random.choice(options)
        starting_position = np.array([option["x"], option["y"], random.choice(range(2000, 5000))])
        return starting_position

    def reduce_amount_of_fuel(self):
        self.time_of_remaining_fuel -= timedelta(minutes=1)

    def explore_the_nearest_space(self):
        pass

    def airplane_collision(self):
        pass

    def update_fuel_reserves_status(self):
        if self.time_of_remaining_fuel > timedelta(minutes=90):
            self.fuel_reserves_status = "GREEN"
        elif self.time_of_remaining_fuel > timedelta(minutes=60):
            self.fuel_reserves_status = "YELLOW"
        elif self.time_of_remaining_fuel > timedelta(minutes=30):
            self.fuel_reserves_status = "RED"
        else:
            self.fuel_reserves_status = "CRITICAL"
    def inform_about_fuel_reserves(self):
        return self.fuel_reserves_status

    def start_landing(self):
        self.is_landing = True

    def cancel_landing(self):
        self.is_landing = False

    def inform_about_successful_landing(self):
        pass

    def count_distance_to_other_airplane(self):
        pass

    def count_distance_to_air_corridor(self):
        pass


class Airplanes:

    def __init__(self):
        self.airplanes = []
