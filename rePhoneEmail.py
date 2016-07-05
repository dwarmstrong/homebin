#!/usr/bin/env python3
# Adapted from "Automate the Boring Stuff with Python / by Al Sweigert"
'''
(O< .: rePhoneEmail.py - Find and extract phone numbers and email addresses
(/)_                     on the clipboard
'''

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

