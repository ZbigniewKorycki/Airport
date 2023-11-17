from runway import Runway


class Airport:

    def __init__(self, width_area=10000, length_area=10000, height_area=5000):
        self.width_area = width_area
        self.length_area = length_area
        self.height_area = height_area
        self.runway_alfa = Runway(start_point_width=0, start_point_length=2000)
        self.runway_beta = Runway(start_point_width=0, start_point_length=8000)
