import random

number = input('Welcome to the World famous guessing game!\n Pick a number from 1-10.\n')

x = random.randint(1, 10)
print(x)

if number == str(x):
  print("You got it right!")
else: 
  print("Sorry you got it wrong :(.  Better luck next time!")


def foo(x, y):
  return "bar"

foo(1, 2)