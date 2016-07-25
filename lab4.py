#1.
def is_digit(char):
    """return the character in to a number

    char -> number"""
    if char in "1234567890":
        return char
    else:
        return "0"

def digit_str(string):
    """return the string in to number

    string -> number"""
    digit_string = ""
    for char in string:
        digit_string = digit_string + is_digit(char)
    return tuple(digit_string)

def digit_num(string):
    """return the sum of all the digits in the the string

    string -> number"""
    total = 0
    for number in digit_str(string):
        total = total + int(number)
    return total


#2.
def longest(s1):
    """return the longest string in tuple

    tuple -> string"""
    s2 = ""
    for string in s1:
        if len(string) > len(s2):
            s2 = string
    return s2

#3.
def count_negative(a1):
    """return the number of how many negative number dose the tuple have

    tuple -> number"""
    a = ()
    for number in a1:
        if number < 0:
            a = a + (number,)
    return len(a) 

#4.
def all_odd(b1):
    """determine the number in tuplr is odd

    tuple -> bool"""
    for number in b1:
        if number % 2 == 0:
            return False
    return True

#5.
#a.
def diff_min(min1,min2):
    """return the difference of minutes

    tuple -> number"""
    return abs(int(min1) - int(min2))

#b.
def time_to_str(time):
    """return the string that represents the time span

    tuple -> string"""
    return str(time[0]) + ":" + str(time[1])

#c.
def time_to_minutes(time):
    """return the total number of mintues

    tuple -> number"""
    return time[0] * 60 + time[1]

#d
def minutes_to_time(number):
    """return tuple of minutes

    number -> tuple"""
    a = number // 60
    b = number % 60
    return (a,b)

#e.
def extract_time(time):
    """return a tuplr of two integers representing the integer of hours and the integers of minutes

    string -> tuple"""
    hour = int(time[0:-3])
    minutes = int(time[-2:])
    return (hour,minutes)

#f.
def time_between(timestring1,timestring2):
    """return the difference of time

    tuple -> string"""
    time1 = extract_time(timestring1)
    time2 = extract_time(timestring2)
    timemin1 = time_to_minutes(time1)
    timemin2 = time_to_minutes(time2)
    timemins = diff_min(int(timemin1),int(timemin2))
    time = minutes_to_time(timemins)
    return time_to_str(time)

    
