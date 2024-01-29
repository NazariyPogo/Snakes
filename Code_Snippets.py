#This file contains random snippets of code ready for copy/pasting to avoid rewriting the same useful code everytime

#Code used to take repeatedly as a user for input and make sure it is an integer
def get_user_input():
    while True:
        decision = input("Enter a number: ")
        if decision.isdigit():
            decision = int(decision)
            return decision
        else:
            print("That is an invalid input, please enter a whole number!")

def get_user_int_in_range(bot, top):
    while True:
        decision = input("Enter a number: ")
        if decision.isdigit():
            decision = int(decision)
            if decision >= 1000 and decision <= 9999:
                return decision
        else:
            print("That is an invalid input, please enter a whole number!")
