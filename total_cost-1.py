print("I'll tell you the total cost of your items, to type 'done' to finish")
count = 0
total = 0
number = 1
print("What is the cost for the item # " + str(number) + "?")
cost_input = input()
print("How many item #" + str(number) + " are you buying?")
quantity_input = input()
while cost_input.lower().strip("'!.,") != "done" and quantity_input.lower().strip("'!.,") != "done":
    count = count + int(quantity_input)
    number = number + 1
    total = total + int(cost_input) * int(quantity_input)
    print("What is the cost for the item # " + str(number) + "?")
    cost_input = input()
    if cost_input == "done":
        break
    print("How many item #" + str(number) + " are you buying?")
    quantity_input = input()
    
print("You have purchased " + str(count) + " items, at a total cost of " + str(total))
    
