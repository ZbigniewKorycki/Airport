class Runway:

    def __init__(self, start_coordinate_x, start_coordinate_y, length=2000):
        self.length = length
        self.start_point_localisation = {
            "x": start_coordinate_x,
            "y": start_coordinate_y,
            "z": 0
        }
        self.end_point_localisation = {
            "x": start_coordinate_x,
            "y": start_coordinate_y + length,
            "z": 0
        }

