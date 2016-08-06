#4a.
def modify(str1):
    """take a string and change all "a" in string to 1, "e" in to 2, "i" into 3,
    "o" into 4, "u" into 5

    str -> str"""
    str2 = ""
    for char in str1.lower():
        if char == "a":
            str2 += "1"
        elif char == "e":
            str2 += "2"
        elif char == "i":
            str2 += "3"
        elif char == "o":
            str2 += "4"
        elif char == "u":
            str2 += "5"
        else:
            str2 += char
    return str2

#b.
print("give the filename that you want to change in a source filename:")
source_filename = input("> ")
while True:
    try:
        with open(source_filename) as source_content:
            print("give tht filename that you want to change into a destination filename:")
            dest_filename = input("> ")
            while True:
                try:
                    with open(dest_filename,"w") as dest_content:
                        for line in source_content:
                            line = modify(line)
                            dest_content.write(line)
                    break
                except IOError:
                    print("I can't find this file, please enter a exist file:")
                    dest_filename = input("> ")
        break
    except IOError:
        print("I can't find this file, please enter a exist file:")
        source_filename = input("> ")

