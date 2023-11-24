from setup_logging import setup_logging

class Runway:

    logger = setup_logging('dev')
    def __init__(self, start_coordinate_x, start_coordinate_y, length=2000):
        self.length = length
        self.start_point_localisation = [start_coordinate_x, start_coordinate_y, 0]
        self.end_point_localisation = [start_coordinate_x, start_coordinate_y + length, 0]
        self.is_free = True

    def block_the_runway(self):
        self.is_free = False

    def open_the_runway(self):
        self.is_free = True

