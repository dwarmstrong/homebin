#!/usr/bin/env python3
'''
Adapted from "Automate the Boring Stuff with Python / by Al Sweigert"

Let the Magic 8 Ball peer into the future and retrieve the answer to 
my questions.
'''
import random

messages = ['It is certain',
        'It is decidedly so',
        'Yes',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook not so good',
        'Very doubtful',
        'Destroy the village to save the village',
        'For good times ... Make it Congee Time',
        'Nuke it from orbit ... Its the only way to be sure',
        'Needs more cowbell']

print('(O< .: ' + messages[random.randint(0, len(messages) - 1)])
print('(/)_')
