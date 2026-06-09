# This program determines if a number is even or odd by using a function called is_even().
def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    return n % 2 == 0

main()