import random

intro = "Welcome to the guessing game. You have 10 tries to guess the number that I am thinking of between 1 and 30. \nEach time you make an incorrect guess, we will show it to you in the GRID OF GUESSES. \nYou may keep guessing until you are successful or until you have run out of guesses."
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
    if attempt > 0:
        guess = input("Enter your guessed NUMBER: ")
        while guess.isdigit() == False or int(guess) < 2 or int(guess) > 29:
            guess = input("Please enter a valid number: ")
        return int(guess)
    elif attempt == 0:
        return save_score(attempt)

#3
def update_grid(grid, guess, guesses_made):
    for row in grid:
        for i in range(len(row)):
            if row[i] == '':
                row[i] = guess
                return grid

#4
def provide_feedback(guess, secret_number):
    if guess == secret_number:
        print("\nCongrats, you have won!") 
    elif guess < secret_number:
        print("\nYour number is too small")
    else:
        print("\nYour number is too big")

#5
def save_score(score):
    with open("myScores.txt", "w") as file:
        file.write(f'Final score: {score}\n')

#6
def play_game():
    Goal = random.randint(1, 30)
    lives = 10
    grid = [['' for i in range(4)] for j in range(3)]
    print_grid(grid)
    print(intro)

    for i in range(1,lives +1):
        guess = get_user_guess(lives - i)
        grid = update_grid(grid, guess, lives - i)
        print_grid(grid)
        if lives - i > 0:
            provide_feedback(guess, Goal)
        elif guess == Goal:
            save_score(lives - i)
            print('Congrats, you have won!')
            break
        else:
            save_score(lives - i)
            print('Sorry, you are out of guesses')
#7
def main():
    play_game()

if __name__ == "__main__":
    main()