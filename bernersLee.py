"""A set of classes to support my web script hacks."""

import bs4, pyperclip, requests, smtplib, sys, webbrowser
"""
#!/usr/bin/env python3
# File: Legobox.py
# Modules to support my scripts in $HOME/bin.

import logging, bs4, requests, smtplib

#!/usr/bin/env python3

import logging, bs4, requests, smtplib

logging.basicConfig(level=logging.DEBUG, 
                format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)
"""

class Browser():
    """Super browser powers"""

    def __init__(self):
        self.browser = 'firefox'

    def open_search_tab(self, web_address):
        """Open browser tab for address retrieved from command line arguments 
        or clipboard"""
        if len(sys.argv) > 1:
            # Get search item from command line
            search_item = ' '.join(sys.argv[1:])
        else:
            # Get search item from clipboard
            search_item = pyperclip.paste()

        if self.browser in webbrowser._browsers:
            www = webbrowser.get(self.browser).open
        else:
            www = webbrowser.open

        www(web_address + search_item)

"""
class Watch():

    def __init__(self, checklist, match_element, save_results_to):
        self.checklist = checklist
        self.match_element = match_element
        self.save_results_to = save_results_to

    def watch_for(self):
        '''Check a website for a matching ELEMENT from CHECKLIST''' 
        with open(self.save_results_to, 'w') as f:
            f.write('# Items found\n')
            with open(self.checklist, 'r') as f_search:
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
                        elems = itemWatch.select(self.match_element)
                        if elems[0].getText() != '0':
                            logging.debug('{}'.format(elems[0]))
                            f.write('{}\n'.format(elems[0]))
                        else:
                            f.write('No match.\n')"""

