from datetime import timedelta


class Airplane:
    def __init__(self, width=30, length=40, height=10, minutes_of_remaining_fuel=180):
        self.width = width
        self.length = length
        self.height = height
        self.time_of_remaining_fuel = timedelta(minutes=minutes_of_remaining_fuel)

