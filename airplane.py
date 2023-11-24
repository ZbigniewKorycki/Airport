from datetime import timedelta
from setup_logging import setup_logging
import random


class Airplane:
    logger = setup_logging('dev')

    def __init__(self, width=30, length=40, height=10, minutes_of_remaining_fuel=180):
        self.width = width
        self.length = length
        self.height = height
        self.time_of_remaining_fuel = timedelta(minutes=minutes_of_remaining_fuel)
        self.starting_position = self.get_starting_position()

    def get_starting_position(self):
        options = [{"x": 0, "y": random.choice(range(0, 10000))},
                   {"x": 10000, "y": random.choice(range(0, 10000))},
                   {"x": random.choice(range(0, 10000)), "y": 0},
                   {"x": random.choice(range(0, 10000)), "y": 10000}]
        option = random.choice(options)
        starting_position = {
            "x": option["x"],
            "y": option["y"],
            "z": random.choice(range(2000, 5000))
        }
        return starting_position

    def head_towards_air_corridor(self):
        pass

    def reduce_amount_of_fuel(self):
        pass

    def fly_into_radar_area(self):
        pass

    def explore_the_nearest_space(self):
        pass

    def airplane_collision(self):
        pass

    def inform_about_small_fuel_reserves(self):
        pass

    def start_landing(self):
        pass

    def inform_about_successful_landing(self):
        pass

    def count_distance_to_other_airplane(self):
        pass

    def count_distance_to_air_corridor(self):
        pass


class Airplanes:

    def __init__(self):
        self.airplanes = []
