#The purpose of this program is to allow the user to play a game of cows and bulls

import code_snippets
import random
import math

class Cows_and_bulls:

    play_again = True
    answer = random.randint(1000, 9999)

    def __init__(self) -> None:
        pass

    def evaluate(self, guess):
        score = 0
        answer_list_cow = list(str(self.answer))        #Creates 2 clone lists for finding cows and bulls w/o
        answer_list_bull = list(str(self.answer))           #each calculation affecting the other's
        digit_str = str(guess)

        for x in range(4):

            while digit_str[x] in answer_list_bull:     #Removes all instances of each guess digit and adds a bull for each
                score += 1
                answer_list_bull.remove(digit_str[x])   #removal used to avoid duplicate bulls

            if digit_str[x] == answer_list_cow[x]:      #Replaces each instance of a number in the same index for guess and answer
                score += 9                                  #and adding a cow
                answer_list_cow[x] = 'x'                #replace with 'x' used to avoid duplicate cows

        return score

    def print_guess_res(self, res):         #Has each case for plurality depending on count of cows and bulls
        cows = math.floor(res / 10)
        bulls = res % 10

        if cows == 1 and bulls == 1:
            print("1 cow, 1 bull")              #Both singular

        elif cows == 1:
            print(f"1 cow, {bulls} bulls")      #Cow singular

        elif bulls == 1:
            print(f"{cows} cows, 1 bull")       #Bull singular

        else:
            print(f"{cows} cows, {bulls} bulls")#Both plural

    def print_win(self):
        return code_snippets.get_user_input_yn(f"Congrats! The number was {self.answer}. Would you like to try again? (y/n)")



if __name__ == "__main__":
    game = Cows_and_bulls()

    while game.play_again == True:
        guess = code_snippets.get_user_int_in_range(1000, 9999, "\nWelcome to Cows and Bulls, a 4 digit number has been set, try to guess it: ")
        res = game.evaluate(guess)
        game.print_guess_res(res)

        while res != 40:
            guess = code_snippets.get_user_int_in_range(1000, 9999, "Try again!: ")
            res = game.evaluate(guess)
            game.print_guess_res(res)

        game.play_again = game.print_win()