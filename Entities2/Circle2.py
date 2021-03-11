from Entities2.Shape2 import Shape2

# This inherits from Shape, measurement is radius.

class Circle2(Shape2):

    def __init__(self,r,c):
        Shape2.__init__(self, c)
        self.radius = r



# class Circle(Shape):
#
#     def __init__(self, radius, color):
#         self.radius = radius

