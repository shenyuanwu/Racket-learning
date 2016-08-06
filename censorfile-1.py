print("What word should I censor?")
user_input_word = input("> ")

print("What file should I censor?")
user_input_file = input("> ")
while True:
    try:
        with open(user_input_file) as file:
            for line in file:
                if user_input_word in line:
                    print("*This line had a bad word in it, and so has been censored.")
                else:
                    print(line.rstrip("\n"))
            break
    except IOError:
        print("There was an error working with that file. Please choose a different filename.")
        user_input_file = input("> ")

