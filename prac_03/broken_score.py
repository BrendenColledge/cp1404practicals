import random


def main():
    """Program gets a score input and returns a rating"""
    score = int(input("Enter Score: "))
    print(determine_rating(score))


def determine_rating(score):
    """Determines rating based on input"""
    if score < 0 or score > 100:
        return "Invalid score"
    if score > 90 or score == 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


main()
