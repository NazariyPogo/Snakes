#The purpose of this program is to have two players play a game of rock paper scissors, the option to play again exists

class RPS:

    def __init__(self) -> None:
        self.play_again = True

    def combat(p1_input, p2_input):
        if p1_input == p2_input:
            print("It's a tie!")
        if p1_input == 'R':
            if p2_input == 'P':
                print("Player 2 wins!")
            if p2_input == 'S':
                print("Player 1 wins!")
        if p1_input == 'P':
            if p2_input == 'R':
                print("Player 1 wins!")
            if p2_input == 'S':
                print("Player 2 wins!")
        if p1_input == 'S':
            if p2_input == 'R':
                print("Player 2 wins!")
            if p2_input == 'P':
                print("Player 1 wins!")


    def ask_if_playing_again(self):
        while True:
            decision = input("Press 0 to end the game or 1 to play again!")
            if len(decision) >= 1 and decision.isdigit():
                if int(decision) == 0:
                    self.play_again = False
                    break
                elif int(decision) == 1:
                    self.play_again = True
                    break
            print("That is an invalid input, please enter 0 or 1!")

    def get_player_choice():
        while True:
            player_choice = input("Please enter R for Rock, P for Paper, or S for Scissors: ")
            if player_choice == 'R' or player_choice == 'P' or player_choice == 'S':
                return player_choice
            else:
                print("That is an invalid input, please enter R, P, or S!")



game = RPS()

while game.play_again == True:
    print("\nHi! Welcome to Rock-Paper-Scissors!\n")

    print("Player 1: ")
    p1_choice = RPS.get_player_choice()

    print("Player 2: ")
    p2_choice = RPS.get_player_choice()

    RPS.combat(p1_choice, p2_choice)

    game.ask_if_playing_again()
