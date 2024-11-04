"""
Question 2

#shoutout to my friend copilot for helping me with this one with #1 and #3

"""
import random
intro = "Welcome to the guessing game. You have 10 tries to guess the number that I am thinking of between 1 and 30. \nEach time you make an incorrect guess, we will show it to you in the GRID OF GUESSES. \nYou may keep guessing until you are successful or until you have run out of guesses."
Goal = random.randint(2,29)
grid = [['' for i in range(4)] for j in range(3)]

#1
def print_grid(grid):
    print("GRID OF GUESSES")
    print("-------------------")
    for row in grid:
        for num in row:
            print(num, end=" | ")
        print("\n-------------------")

#2
def get_user_guess(attempt):
    try:
        if int(attempt) > 1 and int(attempt) < 30:
            return int(attempt)
    except ValueError:
        return "Please enter a valid number between 1 and 30"

#3
def update_grid(grid, guess, guesses_made):
        guesses_made += 1
        for row in range(len(grid)):
            for num in range(row):
                if num == '':
                    num = guess
                    return grid

#4
def provide_feedback(guess, secret_number):
    if guess == secret_number:
        return "Congrats, you have won!"
    elif guess < secret_number:
        return "Your number is too big. Try again"
    else:
        return "Your number is too small. Try again"

#5
def save_score(score):
    with open("myScores.txt", "w") as file:
        file.write(str(score))

#6
def play_game():
    grid = [[''for i in range(4)] for j in range(3)]
    guesses_made = 0
    print(intro)
    print_grid(grid)
    while guesses_made < 10:
        guess = get_user_guess(input("Enter your guessed NUMBER: "))
        grid = update_grid(grid, guess, guesses_made)
        print_grid(grid)
        feedback = provide_feedback(guess, Goal)
        print(feedback)
        if feedback == "Congrats, you have won!":
            save_score(guesses_made)
            break
    save_score(guesses_made)


#7
def main():
    play_game()

if __name__ == "__main__":
    main()
