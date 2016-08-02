#1.
def all_above(num_list,num_given=0):
    """determin all the number in the list is greater that given number
    num_given defaults to 0

    list, num -> bool
    list -> bool"""
    for number in num_list:
        if num_given >= number:
            return False
        return True

#2.
def skip_string(string,skip_amount=(-1)):
    """return the string strat with first letter and skip skip_amount letter each time
    skip_amount defaults to -1

    str,num -> str
    str -> str"""
    i = 0
    str1 = ""
    if skip_amount > 0:
        while 0 <= i < len(string):
            str1 = str1 + string[i]
            i = i + skip_amount + 1
        return str1
    return string[0] * string.count(string[0],0,len(string))

#3.
def get_user_input(lst,bol=False):
    """return the user input if it is exist

    list, bool -> print"""
    print("Please select one of the following:")
    i = 0
    while i < len(lst):
        print(lst[i])
        i = i + 1
    user_input = input(">")
    if bol is True:
        while user_input not in lst:
            print("That wasn't a valid option. Please make a different choice.")
            user_input = input(">")
        lst.clear()
        return user_input
    if bol is False:
        while user_input.lower() not in lst:
            print("That wasn't a valid option. Please make a different choice.")
            user_input = input(">")
        lst.clear()
        return user_input.lower()
            














    
