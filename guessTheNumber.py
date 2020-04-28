#!/usr/bin/env python3
#
# DESCRIPTION="This is a guess-the-number game."

# Adapted from https://automatetheboringstuff.com/2e/chapter2/

import random

min_num = 1
max_num = 100
secret_num = random.randint(min_num, max_num)
chances = 6 # number of guesses

print(f'I am thinking of a number between {min_num} and {max_num}.',
      f'You have {chances} chances to guess what it is.')
for guess_num in range(0, chances):
    print('Take a guess:')
    guess = int(input())
    if guess < secret_num:
        print('Your guess is too low.')
    elif guess > secret_num:
        print('Your guess is too high.')
    else:
        break   # This condition is the correct guess.

if guess == secret_num:
    print('Good stuff! You guessed my number in ' + str(guess_num)
          + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secret_num) + '.')
