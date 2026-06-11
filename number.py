#This is an error handling code using try-except block
while True:
    try:
        x = int(input("Enter a number: "))    
    except ValueError:
        pass
    else:
        break
print(f"The number is {x}")