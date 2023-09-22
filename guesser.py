# import the random library
import random


def guess(x):
    # randomly pick a number from 1, x inclusive
    random_number = random.randint(1, x)
    guess = 0

    # the minute we guess the random number...
    # we break out of the loop
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}"))

        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print("Sorry, guess again, Too high")

    print(f"Yay, congrats, You have guessed the number {random_number}")


def computer_guess(x):
    """In this case, the computer will be guessing
    the number"""
    low = 1
    high = x
    feedback = ''

    while feedback != 'c' :
        if low != high:
            # computer guesses a number between the upper and lower bound
            guess = random.randint(low, high) 
        else:
            guess = low
        # converts input string to lowercase
        feedback = input(
            f'Is {guess} too high (H), or too Low (L), or correct (C)').lower()
        # in the case of upper bound or lower bound...
        # we have to fix the
        if feedback == "h":
            high = guess - 1
        if feedback == "l":
            low = guess + 1

    print(f"Yay, the computer guessed your number, {guess}, correctly!")


computer_guess(500)
