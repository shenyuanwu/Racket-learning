#1.
def string_smash(tup):
    """return the word connect by string in the given tuple

    tuple -> string"""
    tup_len = len(tup)
    showup = "" 
    for string in tup:
        if type(string) is str:
            showup = showup + string
    return showup

#2.
def filter_int(tup):
    """return a tuple consisting of all the integers in the tuple

    tuple -> tuple"""
    tup_len = len(tup)
    showup = ()
    for string in tup:
        if type(string) is int:
            showup = showup + (string,)
    return showup

#3
def all_integers(tup):
    """determine all the items in the tuple are integer

    tuple -> bool"""
    tup_len = len(tup)
    showup = ()
    for string in tup:
        if type(string) is int:
            showup = showup + (string,)
    if len(showup) != len(tup):
        return False
    return True

#4.
def half(argument):
    """return the half of the integer if ardument is an integer or floating point number
    return the first half of argument of tuple or sequence

    num -> num, b str -> str, tuple -> tuple"""
    if isinstance(argument, int):
        return int(argument / 2)
    if isinstance(argument, float):
        return float(argument / 2)
    if isinstance(argument, (str,tuple)):
        return argument[0:int(len(argument) / 2)]
























