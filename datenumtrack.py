#!/usr/bin/env python3
#
# datenumtrack.py - retrieve dates and corresponding numbers

import argparse
import os
import sys

def show_description():
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
                "\n  -d, --dates\t\tinteractive prompt for dates range"
                "\n  -f, --file FILE\t/path/to/settings/FILE"
                f"\n\n(O< Source: {git}/homebin/blob/master/datenumtrack.py"
                "\n(/)_")
    print(message)


# TODO

# Read FILE argument

# Detect if any options specified.

# Set any settings specified by file.

# Use regex patterns to retrieve dates and numbers from source file.

# Display columns of data.

# Display bottom line values.

show_description()
