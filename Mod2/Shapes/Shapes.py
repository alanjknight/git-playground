class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width
    
    def to_string(self):
        return self.length, self.width

class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length, length)


class ColouredSquare(Square):
    def __init__(self, length, colour):
        self.colour=colour
        super(Rectangle).__init__(length,length)  

    def to_string(self):
        return self.length, self.width, self.colour

#rect = Rectangle(34,24)
#print (rect.to_string())

#square = Square(34)
#print (square.to_string())

coloured_square = ColouredSquare(34,"Blue")
print(coloured_square.to_string())