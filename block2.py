#1.
class Block:
    """have attributes to store the coordinates of the bottom-left corner
    and the coordinates of the upper-right corner.

    Attributes: SW(tup of num),NE(tup of num)"""

#2.
    def __init__(self,SW,NE):
        """take two pairs* of coordinates (representing the lower-left ("SW")
        and upper-right ("NE") corners)

        Block,tup,tup -> None"""
        self.SW = SW
        self.NE = NE
        
#3.
    def get_corner(self,corner):
        """takes a string representing which corner
        returns a pair* representing the coordinates of that corner.

        Block,str -> tup"""
        if corner == "SW":
            return self.SW
        elif corner == "SE":
            return (self.NE[0],self.SW[1])
        elif corner == "NE":
            return self.NE
        elif corner == "NW":
            return (self.SW[0],self.NE[1])

#4.
    def get_width(self):
        """return the width of block

        Block -> num"""
        return self.NE[0]-self.SW[0]

    def get_height(self):
        """return the width of block

        Block -> num"""
        return self.NE[1]-self.SW[1]

#5.
    def get_center(self):
        """return the center of Block

        Block -> tup"""
        return ((self.SW[0]+self.NE[0])/2,(self.SW[1]+self.NE[1])/2)

#6.
    def __repr__(self):
        """return a string of the format "Block((SW-corner-x, SW-corner-y), (NE-corner-x, NE-corner-y))"

        Block -> str"""
        return "Block((" + repr(self.SW[0]) + ", " +\
               repr(self.SW[1]) + "),(" + repr(self.NE[0]) +\
               ", " + repr(self.NE[1]) + "))"

#7.
    def move(self,move_right,move_up):
        """that takes two numbers representing the distance to move

        Block,num,num -> None"""
        self.SW = (self.SW[0]+move_right,self.SW[1]+move_up)
        self.NE = (self.NE[0]+move_right,self.NE[1]+move_up)
#8.
    def set_size(self,new_width,new_height):
        """takes two numbers representing a new width and a new height and resizes the Block accordingly.

        Block,num,num -> None"""
        self.SW = (SW[0]-new_width/2,SW[1]-new_height/2)
        self.NE = (NE[0]+new_width/2,NE[1]+new_height/2)

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
