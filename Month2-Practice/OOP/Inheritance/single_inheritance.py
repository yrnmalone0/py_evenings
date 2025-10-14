# Create a base class Shape with a method calculate_area().
# Create a subclass Rectangle that inherits from Shape and overrides calculate_area() to calculate the area of a rectangle.

class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)

rectangle = Rectangle(5,5)
print(rectangle.calculate_area())