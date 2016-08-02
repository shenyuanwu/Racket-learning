#2.
def middle(lst):
    """returnts a copy of that list with the first and last items removed.

    list -> list"""
    return lst[1:-1]

#3.
def chop(lst):
    """modifies the list by removing the first and last items

    list -> list"""
    del lst[0]
    del lst[-1]
