#お試し用のファイルです。

class Shape:
    def what_am_i(self):
        print("I am a shape")
        

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return (self.width + self.length) * 2


class Square(Shape):
    square_list = []
    
    def __init__(self, width):
        self.width = width
        self.square_list.append(self.width)
        print("Created!!")

    def calculate_perimeter(self):
        return self.width * 4

    def change_size(self, n):
        self.width += n

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.width, self.width,
                                            self.width, self.width)

square1 = Square(25)
same_square = square1
        
def compare(x,y):
     return x is y
