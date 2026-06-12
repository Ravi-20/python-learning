# This code simulates a coin flip and prints the result, using the modules or import
import random

coin = random.choice(["Heads", "Tails"])
print("The coin landed on:", coin)

#This is the from module import statement
from random import choice

coin = choice(["Heads", "Tails"])
print("The coin landed on:", coin)

#This code generates a random integer between 1 and 10, and then shuffles a list of cards and prints them in random order.
import random

number = random.randint(1, 10)
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)