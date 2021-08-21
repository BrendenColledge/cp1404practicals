sales = float(input("Enter Sales: $"))
while sales > 0 or sales == 0:
    if sales < 1000:
        sales = sales * 0.10
        print(f"Your bonus is ${sales}")
        sales = float(input("Enter Sales: $"))
    else:
        sales = sales * 0.15
        print(f"Your bonus is ${sales}")
        sales = float(input("Enter Sales: $"))
