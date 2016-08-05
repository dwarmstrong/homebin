#!/usr/bin/env python3

import argparse, logging, bs4, requests
from os.path import expanduser

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

def watch_for(checklist, element, save_results_to):
    '''Check a website for a matching ELEMENT from CHECKLIST''' 
    with open(save_results_to, 'w') as f:
        f.write('# Items found\n')
        with open(checklist, 'r') as f_search:
            for line in f_search:
                if line.startswith('http'):
                    logging.debug('{}'.format(line))
                    f.write(line)
                    res = requests.get(line)
                    try:
                        res.raise_for_status()
                    except Exception as exc:
                        logging.debug('{}'.format(exc))
                        f.write('{}\n'.format(exc))
                        continue
                    itemWatch = bs4.BeautifulSoup(res.text, "lxml")
                    elems = itemWatch.select(element)
                    if elems[0].getText() != '0':
                        logging.debug('{}'.format(elems[0]))
                        f.write('{}\n'.format(elems[0]))
                    else:
                        f.write('No match.\n')

if __name__ == '__main__':
    watch_for(watchlist, searchfor, results)
    logging.debug('End of program')
