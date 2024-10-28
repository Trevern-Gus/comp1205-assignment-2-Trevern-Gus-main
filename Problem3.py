"""
Question 3

Create a function englishToSpongecase that will take a string as input and return the string with random alternation between uppercase and lowercase letters.

"""
import random

def englishToSpongecase(p):
    scase = ""
    for i in p:
        if random.randint(0,1) == 0:
            scase += i.upper()
        else:
            scase += i.lower()
    return scase

print(englishToSpongecase("hello world"))

                
