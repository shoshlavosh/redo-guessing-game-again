"""A number guessing game"""
#didn't use the HB file download this time

import random

answer = random.randint(1,100)

print("Hello! Welcome to the Number Guessing Game.")
print()
print("Your task is to guess a randomly chosen number between 1 and 100.")
print()

def guessing_game():
    """Main game loop"""

    guess = int(input("Guess a number. > "))

    guesses = 0

    while guess != answer:

        if guess < answer:
            guesses += 1
            print("Too low! Try again.")
            guess = int(input("Guess a number. > "))

        elif guess > answer:
            guesses += 1
            print("Too high! Try again.")
            guess = int(input("Guess a number. > "))


    print(f"Correct! You guessed the answer in {guesses} tries. You win!")

guessing_game()