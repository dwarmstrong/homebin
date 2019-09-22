#!/usr/bin/env python3
#
# datenumtrack.py - retrieve dates and corresponding numbers

import argparse
import os
import sys

START_DATE = "2019-09-19"
dates = ()
dates_numbers = {'2019-09-19': 68.0, '2019-09-20': 67.13, '2019-09-21': 67.5}

def description():
    git = "https://github.com/vonbrownie"
    message = ("\nNAME"
                "\n  datenumtrack.py - retrieve dates and "
                "corresponding numbers"
                "\n\nSYNOPSIS"
                "\n  datenumtrack.py [OPTION] FILE"
                "\n\nDESCRIPTION"
                "\n  FILE contains settings that establish a range of dates "
                "along with their\n  correponding numbers to be retrieved "
                "from a specified file."
                "\n\n  Output displays two columns: first column for dates "
                "and second column for\n  the numbers. A bottom line displays "
                "the starting value, end value, and\n  average daily change "
                "for the calendar period."
                "\n\nOPTIONS"
                "\n  -h, --help\t\tthis description"
                "\n  -c, --config FILE\t/path/to/configuration"
                "\n  -d, --dates\t\tinteractive prompt for dates range"
                f"\n\n(O< Source: {git}/homebin/blob/master/datenumtrack.py"
                "\n(/)_")
    print(message)

def dates_numbers_diff():
    prev_number = dates_numbers[START_DATE]
    print("\nDate\t\tNumber\t\tDiff")
    for date, number in dates_numbers.items():
        diff = number - prev_number
        prev_number = number
        print(f"{date}\t{number}\t\t{round(diff, 2)}")

# TODO

# read in arguments

# set options from conf file

# calculate range of dates

# construct a regex pattern to retrieve dates and numbers from source file

# build the dictionary

description()
dates_numbers_diff()
