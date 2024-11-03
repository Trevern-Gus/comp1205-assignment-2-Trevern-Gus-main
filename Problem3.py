"""
Question 3

Create a function englishToSpongecase that will take a string as input and return the string with random alternation between uppercase and lowercase letters.

"""
import random as r 

def englishToSpongecase(p):
    scase = ""
    for i in p:
        if ord(i) > 64 and ord(i) < 91 or ord(i) > 96 and ord(i) < 123:
            if r.randint(0,1) == 0:
                scase += i.upper()
            else:
                scase += i.lower()
        else:
            scase += i
    return scase
    

def main():
    text = input("Enter a string: ")
    print(f"The Converted text is:{englishToSpongecase(text)}")

if __name__ == "__main__":
    main()

                
