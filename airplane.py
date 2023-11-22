from datetime import timedelta


class Airplane:
    def __init__(self, width=30, length=40, height=10, minutes_of_remaining_fuel=180):
        self.width = width
        self.length = length
        self.height = height
        self.time_of_remaining_fuel = timedelta(minutes=minutes_of_remaining_fuel)

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



class Airplanes:

    def __init__(self):
        self.airplanes = []