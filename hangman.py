import random
import string
from words import words


def get_valid_word(words):
    # randomly chooses a word from words list
    word = random.choice(words)
    # keep choosing a word until we select one...
    # which doesn't have a - or a '' in it.
    while "-" in word or ' ' in word:
        # once we get a valid word we will break out of the loop.
        word = random.choice(words)

    return word


def hangman():
    # getting a valid word without '-' or ' '
    word = get_valid_word(words)
    # split the word into a set
    word_letters = set(word)  # get a set of letters in the word
    # gets all the alphabets in ABCD
    alphabets = set(string.ascii_uppercase)

    # what the user has guessed already
    # tracker
    used_letters = set()

    while len(word_letters) > 0:
        # letters used
        # so that the player can keep track
        # joins a list into a strings with spaces between
        print("You have used these letters:", ', '.join(used_letters))

        # what the current word is
        # all the letter guessed is shown
        # letters that haven't been guessed is replaced by dashes
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # getting a user input
        user_letter = input('Guess a letter: ').upper()

        # checking if we have guessed the letter before
        if user_letter in alphabets - used_letters:
            # add to list of letters I have used
            used_letters.add(user_letter)
            # if used letter in word letters
            if user_letter in word_letters:
                # remove that word letter from used letter
                word_letters.remove(user_letter)

        # if we have already used/guessed this letter
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again.")

hangman()
# user_input = input("Type something: ")
# print(user_input)
