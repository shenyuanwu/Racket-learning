#2.
print("Please enter a number (enter 'done' when done )")

user_input = input()

count = 0
total = 0
largest = 0
while user_input.lower().strip("'!.,") != "done":
    user_input = float(user_input)
    count = count + 1
    total = total + user_input
    if user_input >= largest:
        largest=user_input
    average = total / count
    print("Please enter a number (enter 'done' when done )")
    user_input = input()

print("You have enter " + str(count) + " numbers.")
print("The sum of all the numbers is " + str(total))
print("The average of all the numbers is " + str(average))
print("The largest number entered is " + str(largest))
