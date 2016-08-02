
print("What is your favorite fruit: jackfruit, grape, or blueberry?")

user_input = input()

while user_input.lower().strip("'.,!?") != "jackfruit" and user_input.lower().strip("'.,!?") != "grape" and user_input.lower().strip("'.,!?") != "blueberry":
    print("That is not a real fruit! Please choose either jackfruit, grape, or blueberry.")
    user_input = input()
if user_input.lower().strip("'.,!?") == "jackfruit":
    print("That's a horrible fruit. I don't like it.")
elif user_input.lower().strip("'.,!?") == "grape":
    print("Grape is tasty!!!")
elif user_input.lower().strip("'.,!?") == "blueberry":
    print("Well, it is ok, but sometime it is sour.")
