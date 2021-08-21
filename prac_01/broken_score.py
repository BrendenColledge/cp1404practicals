score = float(input("Enter Score: "))
if score < 0 or score > 100:
    print("Invalid score")
if score > 90:
    print("Excellent")
elif score < 50:
    print("Bad")
else:
    print("Passable")
