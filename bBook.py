#!/usr/bin/env python3
# Inspired by "Automate the Boring Stuff with Python" / by Al Sweigart
import webbrowser, sys, pyperclip

msg = '''
(O< .: Get book information from command line arguments or clipboard and open
(/)_   web browser and search Amazon and the Toronto Public Library.
'''
library = "https://www.torontopubliclibrary.ca/search.jsp?Ntt="
amazonCa = "https://www.amazon.ca/"
amazonCom = "https://www.amazon.com/"
amzSearch = "s/ref=nb_sb_noss_1?url=search-alias%3Dstripbooks&field-keywords="

if len(sys.argv) > 1:
    # Get book info from command line
    book = ' '.join(sys.argv[1:])
else:
    # Get book info from clipboard
    book = pyperclip.paste()

if 'firefox' in webbrowser._browsers:
    www = webbrowser.get('firefox').open
else:
    www = webbrowser.open

www(library + book)
www(amazonCa + amzSearch + book)
www(amazonCom + amzSearch + book)
