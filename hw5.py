#1.
def case(string):
    """determine words in string are upper or lower or mixed

    string -> string"""
    if string.islower():
        return "lower"
    elif string.isupper():
        return "upper"
    else:
        return "mixed"

#3.
def count_negative(tup):
    """return the number of negative number in tuple

    tuple -> number"""
    count = 0
    tup_len = len(tup)
    i = 0
    while i < tup_len:
        if int(tup[i]) < 0:
            count = count +1
        i = i + 1
    return count
