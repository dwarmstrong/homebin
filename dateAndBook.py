#!/usr/bin/env python3

import argparse, logging, re
from os.path import expanduser
from dateAndY import Logfile

logging.basicConfig(level=logging.DEBUG, 
                format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program')

msg = """
(O< .: Collect books I have read and the dates I finished reading them from my
(/)_   daily logfile and write to a new logfile.
"""

parser = argparse.ArgumentParser(description=msg, 
        formatter_class=argparse.RawTextHelpFormatter)
args = parser.parse_args()

home = expanduser("~")
dailyLog = home + "/share/log/daily.log"
bookLog = home + "/share/log/dateAndBook.log"
date_regex = "^20[0-9][0-9]-\d\d-\d\d"
book_regex = "^[A-Z]"

def book_cleanup(logfile):
    """Remove tags."""
    with open(logfile, 'r') as f:
        searchLines = f.readlines()
    with open(logfile, 'w') as f:
        book = re.compile(r'^(#book\s#read\s)([A-Z])')
        for line in searchLines:
            # Remove tags
            if book.search(line) != None:
                mo = book.search(line)
                line = re.sub(r'^#book\s#read\s', str(mo.group(2)[2:]), line)
                f.write(line)
            else:
                f.write(line)


def main():
    ## Logfile
    log = Logfile(dailyLog, bookLog, date_regex)

    ## Search for dates and books and output to bookLog
    log.date_and_y('^#book.*')
    book_cleanup(bookLog)
    ## Match date with corresponding book or remove dates with no matches
    log.match_date_and_y(book_regex)


if __name__ == '__main__':
    main()
    logging.debug('End of program')
