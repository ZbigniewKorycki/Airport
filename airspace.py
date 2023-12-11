class Airspace:

    def __init__(self, width_area=10000, length_area=10000, height_area=5000):
        self.width_area = width_area
        self.length_area = length_area
        self.height_area = height_area
        self.available_airspace = None

    def reduce_available_airspace(self):
        pass

    def increase_available_airspace(self):
        pass
