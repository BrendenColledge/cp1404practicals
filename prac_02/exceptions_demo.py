"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""


def valid_number():
    get_number = int(input("Enter number: "))
    while get_number == 0:
        print("Can not divide by zero")
        get_number = int(input("Enter Number: "))
    return get_number


try:
    numerator = valid_number()
    denominator = valid_number()
    number = int(input("Enter number: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
Question 1: When a non-integer is entered
Question 2: When the numerator or denominator is 0 
Question 3: By doing a valid number check loop when the values are entered
"""
