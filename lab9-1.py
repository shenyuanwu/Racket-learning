#1.
def count_in_file(filename,string):
    """takes two strings and returns the number of times that the search string occurs in the file

    str,str -> num"""
    num1 = 0
    try:
        with open(filename) as file:
            for line in file:
                num1 += line.count(string)
    except IOError:
        num1 = -1
    return num1

        
#5.
def grep_to_file(source,destination,string):
    """ takes two filenames and a search string.

    str,str,str -> bool"""
    if ".txt" not in destination:
        return False
    while True:
        try:
            with open(source) as sour_content:
                with open(destination,"w") as dest_content:
                    try:
                        for line in sour_content:
                            if string in line:
                                dest_content.write(line)
                        return True
                    except NameError:
                        return False
        except IOError:
            return False

