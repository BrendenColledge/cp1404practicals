import random

NUMBERS_PER_LINE = 6
MIN = 1
MAX = 45


def main():
    """Program that produces sets of random numbers"""
    total_quick_picks = int(input("How many quick picks? "))
    while total_quick_picks < 0:
        print("Invalid number")
        total_quick_picks = input("How many quick picks? ")

    for i in range(total_quick_picks):
        picks = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MIN, MAX)
            while number in picks:
                number = random.randint(MIN, MAX)
            picks.append(number)
        picks.sort()
        print(" ".join("{:2}".format(number) for number in picks))


main()
