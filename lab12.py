class Distance:
    """storing a distance (with one attribute that represents the distance in inches)

    attribute: dist_feet(float),dist_inch(float)"""

    def __init__(self, dist_inch=0, dist_feet=0):
        """takes two arguments (dist_feet and dist_inch) and properly assigns the appropriate values to the appropriate attributes
        dist_feet defaults to 0
        dist_inch defaults to 0

        Distance,float,float -> None"""
        self.dist_feet = dist_feet
        self.dist_inch = dist_inch
        self.dist_total = self.dist_feet * 12 + self.dist_inch
        self.feet = self.dist_total // 12
        self.inch = self.dist_total % 12

    def __repr__(self):
        """returns a strig that represents the given distance

        Distance -> str"""
        return "Distance(" + repr(self.dist_total) + ")"

    def to_inches(self):
        """return the distance as a number of inches

        Distance -> float"""
        return self.dist_total

    def to_feet(self):
        """returns the distance as a number of feet

        Distance -> float"""
        return self.dist_total / 12

    def to_inches_and_feet(self):
        """ returns a tuple of two numbers representing the Distance in feet and inches

        Distance -> tup"""
        return (self.inch,self.feet)

    def __str__(self):
        """returns a string in the format feet'inches"

        Distance -> None"""
        return str(self.feet) + "\'" + str(self.inch) + "''"

    def __eq__(self,other):
        """returns True if self and other represent the same Distance

        Distance,Distance -> bool"""
        return self.dist_total == other.dist_total

    def __gt__(self,other):
        """returns True if self greater other represent Distance

        Distance,Distance -> bool"""
        return self.dist_total > other.dist_total

    def __lt__(self,other):
        """returns True if self less other represent Distance

        Distance,Distance -> bool"""
        return self.dist_total < other.dist_total

    def __ge__(self,other):
        """returns True if self greater or equal other represent Distance

        Distance,Distance -> bool"""
        return self.dist_total >= other.dist_total

    def __le__(self,other):
        """returns True if self less or equal other represent Distance

        Distance,Distance -> bool"""
        return self.dist_total <= other.dist_total

    def __add__(self,other):
        """returns the sum of self and other

        Distance, Distance -> Distance"""
        return Distance(self.dist_total + other.dist_total)

def feet_to_Distance(num_of_feet):
    """that takes a number of feet and returns a new Distance object representing that distance.

    num -> Distance"""
    return Distance(num_of_feet * 12)

