#The purpose of this program is to print out a game board of requested size for tic-tac-toe, chess, go, etc.

import code_snippets

class Game_Board:

    def __init__(self, x_dim, y_dim) -> None:
        self.x_dim = x_dim
        self.y_dim = y_dim
    
    def print_board(self):
        for _ in  range(self.y_dim):
            self.print_floors()
        for _ in  range(self.x_dim):
            self.print_walls()
        

    def print_floors(self):
        print("---")

    def print_walls(self):
        print("|")


if __name__ == "__main__":
    y_dim = code_snippets.get_user_int_in_range(1, 10, "Please enter the height of the game board: ")
    x_dim = code_snippets.get_user_int_in_range(1, 10, "Please enter the length of the game board: ")
    board = Game_Board(x_dim, y_dim)
    board.print_board()