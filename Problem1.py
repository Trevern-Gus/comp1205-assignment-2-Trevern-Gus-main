"""
Question1:

The program needs to:

Accept the numerator and denominator as input from the user.

Determine whether the fraction is proper or improper.

For improper fractions:

Convert the fraction to a mixed fraction (if applicable).

If the fraction can be reduced to an integer (no remainder), display the integer.

Display the result to the user based on the fraction type.
"""

def get_input():
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    return numerator, denominator

def is_proper_fraction(numerator, denominator):
    if numerator < denominator:
        return True
    else:
        return False
    
def convert_to_mixed_fraction(numerator, denominator):
            whole = numerator // denominator
            if numerator % denominator == 0:
                return str(whole)
            else:
                remainder = numerator % denominator
                fraction = f"{whole} + {remainder}/{denominator}"
                return str(fraction)

def display_fraction_type(numerator, denominator):
    if is_proper_fraction(numerator, denominator):
        print(f"{numerator}/{denominator} is a proper fraction.")
    if not is_proper_fraction(numerator, denominator):
        print(f"{numerator}/{denominator} is an improper fraction and it can be written as {convert_to_mixed_fraction(numerator, denominator)}.")

def main():
    numerator, denominator = get_input()
    display_fraction_type(numerator, denominator)

if 'name' == '__main__':
    main()