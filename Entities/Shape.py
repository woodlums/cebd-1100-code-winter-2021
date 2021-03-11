from datetime import *

class Shape:

    def __init__(self, colour, material):
        self.colour = colour
        self.material = material
        self.create_date = date.today()
