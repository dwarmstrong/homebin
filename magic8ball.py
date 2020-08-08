#!/usr/bin/env python3
#
# Return a fortune determined by a randomly generated number.

# Adapted from https://automatetheboringstuff.com/2e/chapter3/

import random

def get_answer(rand_num):
    if rand_num == 1:
        return 'It is certain.'
    elif rand_num == 2:
        return 'It is decidedly so.'
    elif rand_num == 3:
        return 'Yes.'
    elif rand_num == 4:
        return 'Reply hazy try again.'
    elif rand_num == 5:
        return 'Ask again later.'
    elif rand_num == 6:
        return 'Concentrate and ask again.'
    elif rand_num == 7:
        return 'My reply is no.'
    elif rand_num == 8:
        return 'Outlook not so good.'
    elif rand_num == 9:
        return 'Very doubtful.'

print(get_answer(random.randint(1, 9)))
