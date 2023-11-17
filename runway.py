class Runway:

    def __init__(self, start_point_width, start_point_length, width=80, length=3000):
        self.width = width
        self.length = length
        self.start_point = {
            "width": start_point_width,
            "length": start_point_length,
            "height": 0
        }
        self.end_point = {
            "width": start_point_width,
            "length": start_point_length + length,
            "height": 0
        }
