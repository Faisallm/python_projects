import math
import random


class Player:
    """Base player class
    superclass"""

    def __init__(self, letter):
        # letter is either x or o
        self.letter = letter

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class RandomComputerPlayer(Player):
    """Inherits from player
    subclass"""

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    """Inherits from player
    subclass"""

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_score = False
        val = None
        while not valid_score:
            square = input(self.letter + '\'s turn. Input move(0-9):')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_score = True

            except ValueError:
                print("Invalid square. Try again.")

        return val

            except:
