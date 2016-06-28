#!/usr/bin/env python3
# Practice project from "Automate the Boring Stuff with Python / by Al Sweigert"

msg = '''
(O< .: Explore the *Collatz sequence*, sometimes called
(/)_   "the simplest impossible math problem".
'''

def collatz(number):
    if number % 2 == 0:
        x = number // 2
        return x
    else:
        x = 3 * number + 1
        return x

def userInt():
    try:
        myInt = int(input('Enter an integer > '))
        while myInt > 1:
            myInt = collatz(myInt)
            print(myInt)
    except:
        print('\n(O< .: Error ... Number must be an integer!')
        print('(/)_')

print(msg)
userInt()
