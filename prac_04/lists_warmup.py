numbers = [3, 1, 4, 1, 5, 9, 2]
"""
Numbers[0] = 3
Numbers [-1] = 2
Numbers [3] = 1
Numbers [:-1] = [3, 1, 4, 1, 5, 9]
5 in numbers = True
7 in numbers = false
"3" in numbers = false
numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

"""1. Change the first element of numbers to "ten" (the string, not the number 10)"""
numbers[0] = "ten"
"""2. Change the last element of numbers to 1"""
numbers[6] = 1
"""3. Get all the elements from numbers except the first two (slice) """
print(numbers[1:6])
"""4. Check if 9 is an element of numbers"""
print(9 in numbers)
