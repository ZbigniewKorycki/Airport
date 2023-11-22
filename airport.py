from runway import Runway
from airspace import Airspace


class Airport:

    def __init__(self, coordinate_x, coordinate_y,):
        self.localisation = {
            {
                "x": coordinate_x,
                "y": coordinate_y,
                "z": 0
            }
        }
        self.airspace = Airspace()
        self.runway_alfa = Runway(start_coordinate_x=4000, start_coordinate_y=5000)
        self.runway_beta = Runway(start_coordinate_x=6000, start_coordinate_y=5000)
