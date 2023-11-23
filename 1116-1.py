import math

class MyShape:
    def __init__(self, square_side=None, length=None, width=None, radius=None):
        self.square_side = square_side
        self.length = length
        self.width = width
        self.radius = radius

    def getSquareArea(self):
        if self.square_side is not None:
            return self.square_side ** 2
        else:
            return None

    def getRectangleArea(self):
        if self.length is not None and self.width is not None:
            return self.length * self.width
        else:
            return None

    def getCircleArea(self):
        if self.radius is not None:
            return math.pi * (self.radius ** 2)
        else:
            return None

# Create objects
shape1 = MyShape(square_side=5)
shape2 = MyShape(length=4, width=6)
shape3 = MyShape(radius=3)

# Call class methods
square_area = shape1.getSquareArea()
rectangle_area = shape2.getRectangleArea()
circle_area = shape3.getCircleArea()

# Display results
print(f"Square Area: {square_area}")
print(f"Rectangle Area: {rectangle_area}")
print(f"Circle Area: {circle_area}")
