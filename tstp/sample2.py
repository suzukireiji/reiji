#お試し用のファイルです。

import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * self.radius * self.radius

class Triangle:
    def __init__(self, bottom, height):
        self.bottom = bottom
        self.height = height

    def area(self):
        return self.bottom * self.height / 2

class Hexagon:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 6
    
