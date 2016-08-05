#!/usr/bin/env python3

import argparse, logging
from os.path import expanduser
from webWatch import watch_for

logging.basicConfig(level=logging.DEBUG, 
                format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)
logging.debug('Start of program')

msg = '''
(O< .: Check to see if Toronto Public Library has added an item to catalogue.
(/)_
'''

parser = argparse.ArgumentParser(description=msg,
        formatter_class=argparse.RawTextHelpFormatter)
args = parser.parse_args()

home = expanduser("~")
watchlist = home + "/share/log/tplWatch"
searchfor = "total-results"
results = home + "/share/log/tplMatch" 

if __name__ == '__main__':
    watch_for(watchlist, searchfor, results)
    logging.debug('End of program')
