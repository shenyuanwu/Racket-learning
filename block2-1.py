#1.
class Block:
    """have attributes to store the coordinates of the bottom-left corner
    and the coordinates of the upper-right corner.

    """

#2.
    def __init__(self,SW,NE,height=None):
        """take two pairs* of coordinates (representing the lower-left ("SW")
        and upper-right ("NE") corners)

        Block,tup,tup -> None"""
        if height == None:
            self.__SW = SW
            self.__NE = NE
        else:
            self.__SW = (SW[0]-NE/2,SW[1]-height/2)
            self.__NE = (SW[0]+NE/2,SW[1]+height/2)
#3.
    def get_corner(self,corner):
        """takes a string representing which corner
        returns a pair* representing the coordinates of that corner.

        Block,str -> tup"""
        if corner == "SW":
            return self.__SW
        elif corner == "SE":
            return (self.__NE[0],self.__SW[1])
        elif corner == "NE":
            return self.__NE
        elif corner == "NW":
            return (self.__SW[0],self.__NE[1])

#4.
    def get_width(self):
        """return the width of block

        Block -> num"""
        return self.__NE[0]-self.__SW[0]

    def get_height(self):
        """return the width of block

        Block -> num"""
        return self.__NE[1]-self.__SW[1]

#5.
    def get_center(self):
        """return the center of Block

        Block -> tup"""
        return ((self.__SW[0]+self.__NE[0])/2,(self.__SW[1]+self.__NE[1])/2)

#6.
    def __repr__(self):
        """return a string of the format "Block((SW-corner-x, SW-corner-y), (NE-corner-x, NE-corner-y))"

        Block -> str"""
        return "Block((" + repr(self.__SW[0]) + ", " +\
               repr(self.__SW[1]) + "),(" + repr(self.__NE[0]) +\
               ", " + repr(self.__NE[1]) + "))"

#7.
    def move(self,move_right,move_up):
        """that takes two numbers representing the distance to move

        Block,num,num -> None"""
        self.__SW = (self.__SW[0]+move_right,self.__SW[1]+move_up)
        self.__NE = (self.__NE[0]+move_right,self.__NE[1]+move_up)
#8.
    def set_size(self,new_width,new_height):
        """takes two numbers representing a new width and a new height and resizes the Block accordingly.

        Block,num,num -> None"""
        self.__SW = (self.__SW[0]-new_width/2,self.__SW[1]-new_height/2)
        self.__NE = (self.__NE[0]+new_width/2,self.__NE[1]+new_height/2)

print("Creating block1 with center (5,10), width 4, and height 2...")
block1 = Block((5,10),4,2)
print("block1 is now: " + repr(block1) + "\n")

print("The lower-left corner of block1 is at " \
      + str(block1.get_corner("SW")))
print("The upper-right corner of block1 is at " \
      + str(block1.get_corner("NE")))
print("The width of block1 is " + str(block1.get_width()))
print("The height of block1 is " + str(block1.get_height()) + "\n")

print("Moving block1 5 units to the right...")
block1.move(5,0)
print("block1 is now: " + repr(block1))
print("block1 should still have the same height and width...")
print("The width of block1 is " + str(block1.get_width()))
print("The height of block1 is " + str(block1.get_height()) + "\n")

print("I'm about to change the size of block1.")
print("Before the change, the center is at " + str(block1.get_center()))
print("Now, I'm changing the width to 10 and the height to 20.")
block1.set_size(10,20)
print("The width of block1 is now " + str(block1.get_width()))
print("The height of block1 is now " + str(block1.get_height()))
print("The center should not have changed.")
print("The center of block1 is now " + str(block1.get_center()) + "\n")

print("Creating block2 with corners at (0,0) and (3,6)...")
block2 = Block((0,0),(3,6))
print("block2 is now: " + repr(block2) + "\n")

print("The lower-right corner of block2 is at " \
      + str(block2.get_corner("SE")))
print("The upper-left corner of block2 is at " \
      + str(block2.get_corner("NW")))
print("The width of block2 is " + str(block2.get_width()))
print("The height of block2 is " + str(block2.get_height()) + "\n")

print("Moving block2 1 unit to the left and 10 units down...")
block2.move(-1,-10)
print("block2 is now: " + repr(block2))
print("block2 should still have the same height and width...")
print("The width of block2 is " + str(block2.get_width()))
print("The height of block2 is " + str(block2.get_height()))
