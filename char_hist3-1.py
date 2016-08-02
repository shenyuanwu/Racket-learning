#1.
#a.
def in_hist(char, hist):
    hist_keys = list(hist)
    for lst in hist:
        if char in lst:
            return True
    return False
    
def add_to_hist(char,hist):
    if in_hist(char,hist):
        hist[char] = hist[char] + 1
        return hist
    elif not in_hist(char,hist):
        hist[char] = 1
        return hist
    
    
def make_hist(string):
    """ takes a string and makes a new histogram from that string

    string -> histogram"""
    hist = {string[0]:0}
    for char in string:
        add_to_hist(char,hist)
    return hist

def histoprint1(hist):
    """takes a dictionary representing a histogram
    prints out a "graphical" representation of the histogram
    one entry per output line.

    histogram -> None"""
    hist_keys = list(hist)
    for key in hist_keys:
        print(key + ": " + str(hist[key]*"#"))

#b.
def histoprint2(hist):
    """ takes a dictionary representing a histogram
    and prints out a sorted graphical representation of the histogram
    one entry per output line

    histogram -> none"""
    hist_keys = list(hist)
    for key in sorted(hist_keys):
        print(key + ": " + str(hist[key]*"#"))

#c.
def histoprint3(hist,l1=1):
    """takes a dictionary representing a histogram and an integer representing a scaling factor
    print out a sorted graphical representation of the histogram, one entry per output line
    where each hash mark # stands in for several occurrences of the character
    l1 defaults to 1

    histogram, num-> none"""
    hist_keys = list(hist)
    for key in sorted(hist_keys):
        print(key + ": " + str((hist[key]//l1)*"#"))

#d.

def histoprint4(hist,l1=1):
    """takes a dictionary representing a histogram and an integer representing a scaling factor
    print out a sorted graphical representation of the histogram, one entry per output line
    where each hash mark # stands in for several occurrences of the character
    l1 defaults to 1

    histogram, num-> none"""
    hist_keys = list(hist)
    maxn = max(hist.values()) // 75
    if maxn <= 0:
        for key in sorted(hist_keys):
            print(key + ": " + str((hist[key]//l1)*"#"))
    elif maxn > 0:
        for key in sorted(hist_keys):
            print(key + ": " + (hist[key]//l1)//(maxn+1)*"#")
            

#3.
#a.
def file_to_hist(filename):
    """opens the file with the name filename, reads the contents,
    closes the file, and returns the histogram of contents
	
    str -> hitogram"""
    file = open(filename)
    contents = file.read()
    file.close()
    return histoprint4(make_hist(contents))


























    
    









    
