#1.
#a.
def escape_URL_char(char):
    """returm the sting of the char

    char -> str"""
    if char == " ":
        return "+"
    elif char == "/":
        return "%2F"
    elif char == "#":
        return "%23"
    elif char == "=":
        return "%3D"
    else:
        return char

#b.
def escape_URL(string):
    """return the string escape of the original string

    str -> str"""
    escape_URL = ""
    for char in string:
        escape_URL = escape_URL + escape_URL_char(char)
    return escape_URL
#2.
#a.
def is_vowel(char):
    """determine the char is a vowel

    char -> bool"""
    return char in "aeiouAEIOU"

#b.
def has_vowel(string):
    """determine the string has at least one vowel

    str -> bool"""
    for char in string:
        if is_vowel(char):
            return True
    return False

#c.
def all_vowels(string):
    """determine the character in string are all vowel

    str -> bool"""
    for char in string:
        if not is_vowel(char):
            return False
    return True
