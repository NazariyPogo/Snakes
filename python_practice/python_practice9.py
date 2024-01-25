#The purpose of this program is to be a game of higher-lower for the user

import random

class HigherLower:

    def __init__(self) -> None:
        self._answer = random.randint(1, 9) #Can be changed to user-determined
        self.guess_count = 0

    def evaluate(self, guess):
        if guess < self._answer:
            print("\tThe answer is higher!")
        elif guess > self._answer:
            print("\tThe answer is lower!")
        else:
            return self.print_winner_message()

    def get_user_input(self):
        while True:
            decision = input("Enter a number to try and guess it: ")
            if decision == 'exit':
                return decision
            elif decision.isdigit():
                decision = int(decision)
                self.guess_count += 1
                decision = self.evaluate(decision)
                return decision
            else:
                print("That is an invalid input, please enter a whole number!")

    def print_winner_message(self):
        print(f"Congrats! The number was {self._answer}\nIt took you a total of {self.guess_count} attempts\ntype 'exit' to quit or anything else to go again: ")
        return 0


guess = ''
while guess != 'exit':
    
    game = HigherLower()
    guess = ''

    print('''\nWelcome to Hotter-Colder!
        A number has been set.\n''')
    
    while guess != 0 and guess != 'exit':
        guess = game.get_user_input()
    if guess != 'exit':
        guess = input()