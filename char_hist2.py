#3.
#a. *histogram* is a string of two-item lists show that how many times does
#   character shows in the string

#b.

#c.
def get_freq(char,hist):
    """ takes a character and a histogram 
    returns the frequency associated with that character in the given histogram

    str, histogram -> num"""
    d1_keys = list(hist)
    for key in d1_keys:
        if char in key:
            return hist[char]
            break
    return 0
        
#d.
def in_hist(char, hist):
    hist_keys = list(hist)
    for lst in hist:
        if char in lst:
            return True
            break
        return False
    
def add_to_hist(char,hist):
    if in_hist(char,hist):
        hist[char] = hist[char] + 1
    elif not in_hist(char,hist):
        hist[char] = 1
    
def make_hist(string):
    """ takes a string and makes a new histogram from that string

    string -> histogram"""
    for char in string:
        add_to_hist(char,hist)
    return hist















        
