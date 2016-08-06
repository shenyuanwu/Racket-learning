#1.
def halve(argu):
    """takes an argument of any type and returns half of that argument.

    any -> any"""
    while True:
        try:
            return argu / 2
        except TypeError:
            try:
                return argu[0:len(argu)//2]
            except TypeError:
                if argu == None:
                    print("None")
                    break
                else:
                    return argu

#2.
def trigram_printer(filename):
    """takes a string containing a filename.
    The function should open the file with the given name
    display its contents on the screen, three characters at a time
    and then close the file.

    str -> str"""
    file = open(filename)
    contents = file.read()
    while len(contents) != 0:
        print(contents[0:3])
        contents = contents[3:]
    file.close

#3.
def ngram_printer(filename,numb):
    """takes a string containing a filename.
    The function should open the file with the given name
    display its contents on the screen, three characters at a time
    and then close the file.

    str -> str"""
    try:
        file = open(filename)
        contents = file.read()
        while len(contents) != 0:
            print(contents[0:numb])
            contents = contents[numb:]
        file.close 
    except FileNotFoundError:
        print("I'm sorry, but I could not find a file with that name.")

#5.
def is_anagram(str1,str2):
    """ takes two strings and returns True if the strings are anagrams of each other. 

    strings -> bool"""
    if str1.lower() == str2.lower():
        return False
    return sorted(str1.lower()) == sorted(str2.lower())

def find_anagrams(string):
    """takes a string
    returns a list of anagrams for that string from the wordlist.txt file

    str -> str"""
    words=[string]
    file1 = open("wordlist.txt")
    line = file1.readline().split("\n")
    while len(line[0])!=0:
        if is_anagram(string,line[0]):
            words.append(line[0])
        line = file1.readline().split("\n")       
    return words

        





    
