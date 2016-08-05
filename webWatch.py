#!/usr/bin/env python3

import logging, bs4, requests

logging.basicConfig(level=logging.DEBUG, 
                format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)
logging.debug('Start of program')

msg = '''
(O< .: Functions to support web scraping.
(/)_
'''

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

logging.debug('End of program')
