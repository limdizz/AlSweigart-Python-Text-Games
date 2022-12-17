# Guessing numbers game
import random

guessesTaken = 0

print("Hello! What's your name?")

myName = input()

number = random.randint(1, 100)
print('Well, ' + myName + '. I will think a number from 1 to 100.')

for guessesTaken in range(10):
    print('Try to guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your number is too small.')

    if guess > number:
        print('Your number is too big.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('All right, ' + myName + '! You did it in ' + guessesTaken + ' tries!')

if guess != number:
    number = str(number)
    print('Well. I thought a number ' + number + '.')