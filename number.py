try:
    x = int(input("Enter a number: "))
    print(f"The number is {x}")
except ValueError:
    print("That's not a valid number.")