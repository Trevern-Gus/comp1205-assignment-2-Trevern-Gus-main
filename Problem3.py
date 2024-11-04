"""
Question 3

Create a function englishToSpongecase that will take a string as input and return the string with random alternation between uppercase and lowercase letters.

"""
import random as r

def englishToSpongecase(p):
    sp = ''
    for i in p:
        if r.choice([True,False]):
            sp += i.upper()
        else:
            sp += i.lower()
    return sp

def main():
    text = input("Enter a string: ")
    print(f"The Converted text is:{englishToSpongecase(text)}")

if __name__ == "__main__":
    main()

                
