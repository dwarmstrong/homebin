#!/usr/bin/env python3
#
# DESCRIPTION="Simplest impossible math problem"

def description():
    name = 'Collatz Sequence'
    description = 'the simplest impossible math problem'
    print('----[ ' + name + ' - ' + description + ' ]----')

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1

def user_num():
    select = 0  # 0 = no integer, 1 = integer
    steps = 0   # number of calculations performed to arrive at 1
    while select == 0:
        try:
            print('\nEnter an integer:')
            num = int(input())
            select = 1
        except:
            print('Error: User must enter an integer.')
    while num > 1:
        # sooner or later, starting with any integer and
        # using this sequence, it will arrive at 1
        num = collatz(num)
        steps += 1
        print(str(num))
    if steps == 1:
        # if user entered a 2, only a single step required to arrive at 1
        print('*Calculated in 1 step.')
    else:
        print('*Calculated in ' + str(steps) + ' steps.')

description()
user_num()
