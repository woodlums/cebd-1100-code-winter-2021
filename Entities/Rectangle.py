from Entities.Square import Square


# This inherits from Shape
class Rectangle(Square):

    def __init__(self, colour, material, bottom_side, right_side):

        self.right_side = right_side

        super().__init__(colour, material, bottom_side)

    def area(self):

        return self.bottom_side * self.right_side

    def perimeter(self):

        return (self.bottom_side + self.right_side) * 2
