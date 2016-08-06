print("give the filename that you want to copy in a source filename:")
source_filename = input("> ")
while True:
    try:
        with open(source_filename) as source_content:
            print("give tht filename that you want to copy in a destination filename:")
            dest_filename = input("> ")
            while True:
                try:
                    with open(dest_filename,"w") as dest_content:
                        for line in source_content:
                            dest_content.write(line)
                    break
                except IOError:
                    print("I can't find this file, please enter a exist file:")
                    dest_filename = input("> ")
        break
    except IOError:
        print("I can't find this file, please enter a exist file:")
        source_filename = input("> ")


