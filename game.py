"""A number guessing game"""

import random

answer = random.randint(1,100)

print("Hello! Welcome to the Number Guessing Game.")
print()
name = input("Please enter your name. > ")
print()
print(f"Hello, {name}! Your task is to guess a randomly chosen number between 1 and 100.")
print()

def guessing_game():
    """Main game loop"""

    guess = int(input("Guess a number. > "))

    guesses = 0

    while guess != answer:

        if guess > 100 or guess < 1:
            print("Please choose a number between 1 and 100.")
            guess = int(input("Guess a number. > "))

        elif guess < answer:
            guesses += 1
            print("Too low! Try again.")
            guess = int(input("Guess a number. > "))

        elif guess > answer:
            guesses += 1
            print("Too high! Try again.")
            guess = int(input("Guess a number. > "))


    print(f"Correct! Great job, {name}, you guessed the answer in {guesses} tries. You win!")

guessing_game()