"""
Question 3

Create a function englishToSpongecase that will take a string as input and return the string with random alternation between uppercase and lowercase letters.

"""
import random as r

def englishToSpongecase(p):
    scase = ""
    uppercase = True 
    rand = r.randint(0,1)
    if rand == 0:
        scase += p[0].upper()
        uppercase = False
    else:
        scase += p[0].lower()
        uppercase = True
    for i in range(1,len(p)):
        if uppercase:
            scase += p[i].upper()
            uppercase = False
        else:
            scase += p[i].lower()
            uppercase = True
    return scase

def main():
    text = input("Enter a string: ")
    print(f"The Converted text is:{englishToSpongecase(text)}")

if __name__ == "__main__":
    main()

                
