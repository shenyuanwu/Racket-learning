print("Add as many items to the basket as you want. When you're done, enter")
print("'nothing'.")
user_input = input('What do you want to put into the basket now? ')
lst = []
count = 0 
while user_input.lower().strip("'/?.,!") != 'nothing':
    count = count + 1
    lst.append(user_input)
    print("Okay")
    user_input = input('What do you want to put into the basket now? ')
print("There are " + str(count) + " items in the basket:")
number = 0


while number < len(lst):
    print("Item " + str(number + 1) + ": " + str(lst[number]))
    number = number + 1
