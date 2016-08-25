#!/usr/bin/env python3
# Inspired by "Automate the Boring Stuff with Python" / by Al Sweigart
from bernersLee import Browser

msg = '''
(O< .: Get a street address from command line arguments or clipboard and open
(/)_   web browser to the Google Maps page for the address.
'''

def main():
    browser = Browser()
    browser.open_search_tab('https://www.google.com/maps/place/')

main()
