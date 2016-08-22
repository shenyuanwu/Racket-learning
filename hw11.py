#2.
def factorial(x):
    """takes a natural number and returns the product of all the natural numbers from 1 up to the given number.

    natural num -> num"""
    if x == 0:
        return 0
    elif x == 1 :
        return 1
    else:
        return x * factorial(x-1)

#3.
def power_of_two(x):
    """takes a natural number n and returns 2^n

    natural num -> num"""
    if x == 0:
        return 1
    elif x == 1 :
        return 2
    else:
        return 2 * power_of_two(x-1)

#4.
def power(b,n):
    """takes a natural number n and returns b^n

    natural num -> num"""
    if b == 0:
        return 0
    else:
        if n == 0:
            return 0
        elif n == 1 :
            return b
        else:
            return b * power(b,n-1)

#5.
#A Binary Number Tree (BNT) is one of:
# - 1
# - ((1,(2,3)),4)
#A Binary Number Tree (BNT) is one of:
# - 2
# - (4,(1,(3,2)))
#A Binary Number Tree (BNT) is one of:
# - 3
# - (1,(2,(3,4)))


#7.
def add_leaves(tree):
    """returns the sum of the number of leaves in tree
	
    BNT -> int"""
    if isinstance(tree,tuple):
            return add_leaves(tree[0]) + add_leaves(tree[1])
    else:
            return tree
