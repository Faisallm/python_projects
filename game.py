

class TicTacToe:

    def __init__(self):
        # we will use a single list to represent a 3 x 3 board
        # list comprehension
        self.board = [" " for _ in range(9)]
        # tracks the current winner of the game
        self.current_winner = None

    def print_board(self):
        # 0-3, 3-6, 6-9 (how we will iterate the rows of the board)
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + " | ".join(row) + " |")

    # a static method can be called without an object for that class.
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + " | ".join(row) + " |")


    def available_moves(self):

        return [i for i, spot in enumerate(self.board) if spot == " "]
        # # return
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)

