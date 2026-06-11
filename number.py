#This is an error handling code using try-except block
while True:
    try:
        x = int(input("Enter a number: "))    
    except ValueError:
        print("That's not a valid number.")
    else:
        break
print(f"The number is {x}")