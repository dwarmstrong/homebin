#!/usr/bin/env python3
# Inspired by "Automate the Boring Stuff with Python" / by Al Sweigart
import webbrowser, sys, pyperclip

msg = '''
(O< .: Get a street address from command line arguments or clipboard and open
(/)_   web browser to the Google Maps page for the address.
'''

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
