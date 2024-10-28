"""
Question 2

"""
import random
intro = "Welcome to the guessing game. You have 10 tries to guess the number that I am thinking of between 1 and 30. \nEach time you make an incorrect guess, we will show it to you in the GRID OF GUESSES. \nYou may keep guessing until you are successful or until you have run out of guesses."
Goal = random.randint(1,30)

def get_user_guess():
    p = input("Enter your guess: ")
    return p
