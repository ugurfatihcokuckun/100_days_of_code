from art import logo
import random

def guess_the_number():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    numb = random.randint(1,100)
    print(f"Pssst, the correct answer is {numb}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n")

    if difficulty == "easy":
        lives = 10
        print("You have 10 attempts remaining to guess the number.")
    elif difficulty == "hard":
        lives = 5
        print("You have 5 attempts remaining to guess the number.")
    while lives > 0:
        
        guess = int(input("Make a guess: \n"))
        if guess == numb:
            lives = 0
            print(f"You got it! The answer was {numb}.")

        elif guess < numb:
            print("low\nGuess again")
            print(f"You have {lives} attempts remaining to guess the number.")
            lives -= 1
        elif guess > numb:
            print("high\nGuess again")
            print(f"You have {lives} attempts remaining to guess the number.")

guess_the_number()
    
again = input("play again yes or no: ")
if again == "yes":
    guess_the_number()
else:
    print("Good bye!")