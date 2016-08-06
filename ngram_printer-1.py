print("How many characters should I display at a time?")
user_input_numb = input("> ")
while True:
    print("What file should I display?")
    user_input_filename = input("> ")
    try:
        file = open(user_input_filename)
        contents = file.read()
        while len(contents) != 0:
            print(contents[0:int(user_input_numb)])
            contents = contents[int(user_input_numb):]
        file.close
        break
    except FileNotFoundError:
        print("I couldn't read from that file. Please try a different filename.")

