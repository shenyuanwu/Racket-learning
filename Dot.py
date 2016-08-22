import math
#3.
import turtle
turtle.penup()
turtle.speed(0)
#1.
class Dot:
#a.
    """storing information about a dot on a flat grid

    attributes: xposition(int),yposition(int),color(str)"""
#b.
    def __init__(self,xposition,yposition,color):
        """takes three arguments (x-position, y-position, and color) and properly assigns the appropriate values to the appropriate attributes

        Dot,int,str -> None"""
        self.xposition = xposition
        self.yposition = yposition
        self.color = color
#c.
    def __repr__(self):
        """return a string of the form Dot(xposition,yposition,color)

        Dot -> str"""
        return "Dot(" + repr(self.xposition) + ", " \
               + repr(self.yposition) + ", " + repr(self.color) + ")"
#d.
    def move_up(self,up_unit):
        """move Dot up up_unit unit

        int -> None"""
        self.yposition = self.yposition + up_unit

    def move_right(self,right_unit):
        """move Dot right right_unit unit

        int -> None"""
        self.xposition = self.xposition + right_unit
#e.
    def distance_to(self,Dot2):
        """takes a second Dot and returns the distance from the original Dot to that second Dot

        Dot2 -> num"""
        return math.sqrt((Dot2.xposition - self.xposition) ** 2 + (Dot2.yposition - self.yposition) ** 2)
#3c.
    def draw(self):
        """takes no extra arguments and draws an appropriately colored dot at the Dot's coordinates with a 5-pixel diameter.

        Dot -> None"""
        turtle.dot(5,self.color)
        turtle.goto(self.xposition,self.yposition)
#2.
#a.
Dot1 = Dot(30,60,"pink")
Dot2 = Dot(37,64,"red")
Dot3 = Dot(100,100,"black")
#b
Dot1.move_up(5)
Dot2.move_up(-2)
#c.
Dot1.move_right(5)
Dot2.move_right(-4)
#d.
Dot3 = Dot(100,100,"yellow")
#e.
print(Dot1.distance_to(Dot2))


#3d.
print("Draw a dot with self color")
Dot1.draw()
Dot2.draw()
Dot3.draw()

    

