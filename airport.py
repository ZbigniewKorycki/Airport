from runway import Runway

class Airport:

    def __init__(self, width=10000, length=10000, height=5000):
        self.width = width
        self.length = length
        self.height = height
        self.runway_alfa = Runway()
        self.runway_beta = Runway()
