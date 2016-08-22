#1.
class Thing:
    """representing physical objects in the game

    Attribute: name(str),location(str)"""

    def __init__(self,name,location):
        """take the name of object and the location of object

        Thing,str,str -> None"""
        self.name = name
        self.location = location

    def __repr__(self):
        """repersent the string og the name and location

        Thing -> str"""
        return "Thing(" + repr(self.name) + ", " + repr(self.location) \
               + ")"

    def description(self):
        """return a string that describes the object

        Thing -> str"""
        return "The " + self.name + " is " + self.location + "."
    
#2.
class Openable(Thing):
    """representing those physical objects that can be opened.

    Attribute:is_open(boolean)"""

    def __init__(self,name,location,is_open = False):
        """take the name of object and the location of object and
        use is_open to represents whether or not the object is open

        Openable,str,str,bool -> None"""
        super().__init__(name,location)
        self.is_open = is_open

    def description(self):
        """return a string that shows the name location is open or close

        Openable -> str"""
        super().description()
        if self.is_open == False:
            return "The " + self.name + " " + self.location + " is closed."
        elif self.is_open == True:
            return "The " + self.name + " " + self.location + " is open."

    def try_open(self):
        """open the thing are close and return True and let open object
        still be open and return False

        Openable -> bool"""
        if self.is_open == False:
            self.is_open = True
            return True
        elif self.is_open == True:
            return False

#3.
class Lockable(Openable):
    """representing physical objects that can be unlocked and opened.

    Attribute:key:(str),is_locked:(bool)"""
    
    def __init__(self,name,location,key,is_open=False,is_locked=False):
        """take the name of object and the location of object and
        use is_open to represents whether or not the object is open
        and a key,  and check if the key can unlocked it

        Lockable,str,str,str,bool,bool"""
        super().__init__(name,location,is_open = False)
        self.key = key
        self.is_locked = is_locked

    def description(self):
        """return a string that shows the name location is open or close and
        locked or unlocked

        Openable -> str"""
        super().description()
        if self.is_open == False:
            if self.is_locked == False:
                return "The " + self.name + " " + self.location + \
                       "is closed but unlocked."
            elif self.is_locked == True:
                return "The " + self.name + " " + self.location + \
                       "is locked."
        elif self.is_open == True:
            return "The " + self.name + " " + self.location + " is open."

    def try_open(self):
        """unlocked the thing are close and return True and
        originally locked or if it was already open return False

        Openable -> bool"""
        if self.is_open == False:
            if self.is_locked == False:
                self.is_open = True
                return True
        else:
            return False

    def try_unlock_with(self,Thing_key):
        """checkif the key can unlocked  the door

        is_Locked,str -> bool"""
        if self.is_open == True:
            return False
        elif self.is_open == False:
            if self.is_locked == True:
                if Thing_key == self.key:
                    self.is_locked = False
                    return True
                else:
                    return False
            else:
                return False
        





























