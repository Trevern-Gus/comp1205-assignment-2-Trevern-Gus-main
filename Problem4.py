"""
Question 4 

"""
import random as r

intro = "Hacking Minigame\nFind the password in the computer's memory. You are given clues after each guess.\nFor example, if the secret password is MONITOR but the player guessed CONTAIN,\nthey are given the hint that 2 out of 7 letters were correct.\n\nPress Enter to begin..."

WORDS = []
games_words = []
chosenwords = []
special_chr = ["!", "@", "#", "$", "%", "^", "&", "*", "~"]
lives = 4

def loadWords():
    global WORDS
    try:
        with open("sevenletterwords.txt", 'r') as f:
            for word in f:
                word = word.strip()
                if len(word) == 7:
                    WORDS.append(word)
            return WORDS
    except:
        Exception
        print("File not found")
        return []

def getWords():
    global game_words
    global chosenwords
    r.shuffle(WORDS)
    game_words = r.sample(WORDS, 12)
    chosenwords.insert(0, game_words[0])
    chosenwords =+ r.sample(game_words, 3)
    
    

def getComputerMemoryString():
    global chosenwords
    num = ['0x12A4', '0x22B4', '0x12B4', '0x22C4']
    memstring = ''
    for i in range(4):
        rubbish7 = ''.join(r.sample(special_chr, 7))
        index = r.randint(0, 5)
        part1, part2 = rubbish7[:index], rubbish7[index:]
        rubbishmem = part1 + chosenwords[i] + part2
        memstring += num[i] + ' ' + rubbishmem + ' '
        if i == 1:
            memstring += '\n'
    return memstring
    

def askForPlayerGuess(chosenwords, guess_no):
    while True:
        guess = input(f"Enter password: ({guess_no} tries remaining)").upper()
        if guess in chosenwords:
            return guess
        else:
            print("Invalid password")
            
def numMatchingLetters(guess, password):
    global lives
    lives -= 1
    count = 0
    for i in range(len(password)):
        if guess[i] == password[i]:
            count += 1
    return count
    
      

def main():
    global chosenwords 
    global lives

    print(intro)
    loadWords()
    getWords()
    print(f"{getComputerMemoryString()}\n...\n")
    while lives > 0:
        guess = askForPlayerGuess(chosenwords, lives)
        num = numMatchingLetters(guess, chosenwords[0])
        print(num)
        if numMatchingLetters(guess, chosenwords[0]) == 7:
            print("A C C E S S G R A N T E D")
            break
        else:
            print(f'Access Denied ({num}/7 correct)')
    if lives == 0:
        print(f"Out of tries. Secret password was {chosenwords[0]}")

if __name__ == "__main__":
    main()
