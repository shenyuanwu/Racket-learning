#1.
#a.*histogram* is a list of two-item lists show that how many times does
#   character shows in the string

#b.
def in_hist(char,hist):
    """takes a character and a histogram and determines whether the character
    is listed in the histogram

    str, histogram -> bool"""
    for lst in hist:
        if char == lst[0]:
            return True
            break
    return False

#c.
def add_to_hist(char,hist):
    """takes a character and a histogram and adds an occurrence of that
    character to the histogram

    str, histogram -> histogram"""
    if in_hist(char,hist):
        for lst in hist:
            if char == lst[0]:
                lst[1] =lst[1] + 1
    else:
        hist.append([char,1])
            
#d.
def make_hist(string):
    """takes a string and makes a new histogram from that string

    str -> histogram"""
    hist = []
    for char in string:
        add_to_hist(char,hist)
    return hist

#e.
def get_freq(char,hist):
    """takes a character and a histogram
    returns the frequency associated with that character in the given histogram

    str, histogram -> num"""
    if in_hist(char,hist):
        for lst in hist:
            if char == lst[0]:
                return lst[1]
    else:
        return 0














