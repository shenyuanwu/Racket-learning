###2.
##def get_user_input(lst):
##    count = 0
##    print("Please select one of the following:")
##    while count < len(lst):
##        print(str(lst[count]))
##        count = count + 1
##    user_input = input(">")
##    if user_input not in lst:
##        print("That wasn't a valid option. Please make a different choice.")
##        user_inpput = input(">")
##    lst = []
##    lst.append(user_input)
##
#3.
def cumulative_sum(lst):
    """return a list of the cumulative sums of those numbers

    list -> list"""
    count = 0
    lst1 = []
    number = 0
    while count < len(lst):
        number = number + int(lst[count])
        lst1.append(number)
        count = count + 1
    return lst1

#4.
def has_duplicates(lst):
    """return Ture if any teo items in the list are equal

    lst -> bool"""
    count = 0
    lst1 = []
    number = 0
    while count < len(lst):
         number = number + 1
         lst1.append(number)
         if lst[count] in lst1:
             return True
         return False
         count = count + 1

#5.
def remove_zeroes(lst):
    """return taking list and remove 0 in the list

    list -> list"""
    while 0 in lst:
        lst.remove(0)
    return lst

###6.
##def without_zeroes(lst):
##    """takes a list of numbers and returns a copy of that
##    list with every occurrence of the number zero removed.
##
##    list -> list"""
##    count = 0
##    lst1 = []
##    numb = []
##    while count < len(lst):
##        if type(lst[count]/10) is int:
##                numb = numb.append(lst(count))
##                while 0 in numb:
##                    numb.remove(0)
##                lst1.append(numb)
##        lst1.append(lst[count])
##        numb.clear()
##        count = count + 1
##    return lst1

###7.
##def remove_duplicates(lst):
##    """takes a list and removes any extra occurrences of values
##    that appear multiple times in the list.
##    
##    list -> list"""
##    count = 0
##    while count < len(lst):
##        if lst[count] in lst:
##        count = count + 1

#8.
def filter_duplicates(lst):
    """takes a list and returns a copy of the list with all duplicate value removed

    list -> list"""
    count = 0
    lst1 = []
    while count < len(lst):
        if lst[count] not in lst1:
            lst1.append(lst[count])
        count = count + 1
    return lst1

#9.
def is_anagram(str1,str2):
    """ takes two strings and returns True if the strings are anagrams of each other. 

    strings -> bool"""
    count = 0
    noun1 = ""
    noun2 = ""
    while count < len(str1):
        noun1 = str1[count]
        noun2 = str2[count]
        if str1.count(noun1, 0, len(str1)) != str2.count(noun2, 0, len(str2)):
            return False
        count = count + 1
    return True

#10
def anagrams_in(string,lst):
    """takes a string and a list of strings and
    returns a list of strings from the list that are anagrams of the given string. 

    string, list -> list"""
    count = 0
    noun = ""
    lst1 = []
    while count < len(lst):
        noun = lst[count]
        if is_anagram(string,noun):
            lst1.append(noun)
        count = count + 1
    return lst1

#11.
def anagram_partition(lst):
    """takes a list of strings,
    returns a list of lists of strings
    where the strings in each list are all anagrams of each other.

    list -> list"""
    count = 0
    noun = ""
    lst1 = []
    lst2 = []
    while count < len(lst):
        noun = lst[count]
        lst.remove(noun)
        if anagrams_in(noun,lst):
            lst1.append(lst)
    return lst1













