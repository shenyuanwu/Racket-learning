#1.
KEYWORD_CATEGORIES = {"happy":["great", "excited", "happy", "awesome"],"uncertain":["maybe", "worried", "dunno"]}
CATEGORY_RESPONSES = {"happy":["I'm glad to hear it!", "That's great!", "I like your attitude."],"uncertain":["No one knows what the future holds.","Don't worry so much.","It'll turn out okay."]}

#2.
def keyword_category(potential_keyword):
    """takes a potential keyword and returns the associated category

    str -> str"""
    key = list(KEYWORD_CATEGORIES)
    for keyword in key:
        if potential_keyword.lower() in KEYWORD_CATEGORIES[keyword]:
            return keyword
    return "undefined"

#3.
def sentence_category(sentence):
    """takes a sentene, breaks it up into words*, checks the category of the words, and returns a category for the sentence

    str -> str"""
    lst = sentence.split()
    lst_result = []
    for word in lst:
        lst_result.append(keyword_category(word))
    if "uncertain" in lst_result:
        return "uncertain"
    elif "happy" in lst_result:
        return "happy"
    else:
        return "undefined"
        
#4.
def category_response(category):
    """ takes a string (a category) and returns a random* sentence chosen from the appropriate list of responses in the CATEGORY_RESPONSES dictionary.

    str -> str"""
    import random

    return random.choice(CATEGORY_RESPONSES[category])

#5.
def chat():
    text = []
    print("Hello, I am a chatbot.")
    user_input = input(">")
    text.append("Hello, I am a chatbot.")
    text.append(user_input)
    while user_input.lower() != "bye":
        while sentence_category(user_input) != "undefined":
            response = category_response(sentence_category(user_input))
            print(response)
            user_input = input(">")
            text.append(response)
            text.append(user_input)
        print("That's interesting")
        user_input = input(">")
        text.append("That's interesting")
        text.append(user_input)
    print("Goodbye! It was nice talking to you.")
    text.append("Goodbye! It was nice talking to you.")
    user_input_dest = input(">> ")
    print(str(text))
    with open(user_input_dest,"w") as dest_content:
        dest_content.write(str(text))
    






