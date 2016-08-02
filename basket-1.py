print("Add as many items to the basket as you want. When you're done, enter")
print("'nothing'.")
user_input = input('What do you want to put into the basket now? ')
list = []
count = 0 
while user_input.lower().strip("'/?.,!") != 'nothing':
    count = count + 1
    list.append(user_input)
    print("Okay")
    user_input = input('What do you want to put into the basket now? ')
print("There are " + str(count) + " items in the basket: " + str(list))
