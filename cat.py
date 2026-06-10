# This program prints "meow" three times using while loop.
print("This is a while loop:")
i = 3
while i != 0:
    print("meow")
    i = i - 1

print("-------------------")

# This program prints "meow" three times using for loop.
print("This is a for loop:")
for i in range(3):
    print("meow")

print("-------------------")

# This program prints "meow" n times, where n is a positive integer entered by the user.
while True:
    n = int(input("Enter a number: "))
    if n > 0:
        break

for _ in range(n):
    print("meow")