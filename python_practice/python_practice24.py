#The purpose of this program is to print out a game board of requested size for tic-tac-toe, chess, go, etc.

import code_snippets
import sys

class Game_Board:

    def __init__(self, x_dim, y_dim) -> None:
        self.x_dim = x_dim
        self.y_dim = y_dim
    
    def print_board(self):
        for _ in range(self.y_dim):     #y is used for number of levels not including floor at bottom
            self.print_floors(x_dim)

            print()

            self.print_walls(x_dim + 1) #Extra wall because all walls share a roof i.e.     --- --- ---   = 3
            print()                     #                                                  |   |   |   |  = 4

        self.print_floors(x_dim)        #Adds final floor at bottom since levels only include a roof and walls
        

    def print_floors(self, amount):
        for _ in  range(amount):
            sys.stdout.write(" ---")

    def print_walls(self, amount):
        for _ in  range(amount):
            sys.stdout.write("|   ")


if __name__ == "__main__":
    y_dim = code_snippets.get_user_int_in_range(1, 20, "Please enter the height of the game board: ")
    x_dim = code_snippets.get_user_int_in_range(1, 20, "Please enter the length of the game board: ")
    board = Game_Board(x_dim, y_dim)
    board.print_board()