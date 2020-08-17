import math
class Rectangle:
    def __init__(self,w,h):
        self.width = w
        self.height = h

    def set_width(self,w):
        self.width = w

    def set_height(self,h):
        self.height = h

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return (2*self.width+2*self.height)

    def get_diagonal(self):
        return ((self.width**2+self.height**2)**.5)

    def get_picture(self):
        str = []
        if(self.height>50 or self.width >50):
            return "Too big for picture."
        else:
            for i in range(self.height):
                for j in range(self.width):
                    str.append('*')
                str.append('\n')
        return ''.join(str)

    def get_amount_inside(self,a):
        return math.floor(self.width/a.width)*math.floor(self.height/a.height)

    def __str__(self):
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"    

class Square(Rectangle):
    def __init__(self,a):
        self.width = a
        self.height = a

    def set_side(self,a):
        self.width = a
        self.height = a

    def set_width(self,a):
        self.width = a
        self.height = a
    
    def set_height(self,a):
        self.width = a
        self.height = a

    def __str__(self):
        return "Square(side="+str(self.width)+")"