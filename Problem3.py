"""
Question 3

Create a function englishToSpongecase that will take a string as input and return the string with random alternation between uppercase and lowercase letters.

"""
import random

def englishToSpongecase(p):
    scase = ""
    for i in range(len(p)):
        if random.randint(0,1) == 0:
            scase += p[i].upper()
        else:
            scase += p[i].lower()
    return scase

def main():
    text = input("Enter a string: ")
    print(f"The Converted text is:{englishToSpongecase(text)}")

if __name__ == "__main__":
    main()

                
