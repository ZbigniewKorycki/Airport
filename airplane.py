from datetime import timedelta


class Airplane:
    def __init__(self, width=60, length=70, height=20, minutes_of_remaining_fuel=180):
        self.width = width
        self.length = length
        self.height = height
        self.time_of_remaining_fuel = timedelta(minutes=minutes_of_remaining_fuel)

