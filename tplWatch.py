#!/usr/bin/env python3

import argparse, logging, os, re, sys
from os.path import expanduser
from webWatch import watch_for, keep_me_posted

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
parser.add_argument("-n", "--notify", 
        help="email notification", action="store_true")
parser.add_argument("-u", "--username", help="SMTP username")
parser.add_argument("-p", "--passwd", help="SMTP password")
args = parser.parse_args()

home = expanduser("~")
watchlist = home + "/share/log/tplWatch"
searchfor = "total-results"
results = home + "/share/log/tplMatch" 

def make_message(trigger, search_results):
    '''Craft a message for SMTP'''
    with open(search_results, 'r') as f:
        message = ""
        report = f.readlines()
        logging.debug('== Results ==\n{}\n'.format(report))
        regex = re.compile(r'.*({}).*'.format(trigger))
        # If the trigger pattern shows up anywhere in the report, return a 
        # message containing the report contents
        if any(regex.search(line) for line in report):
            for line in report:
                message += line
        logging.debug('Message length: {}'.format(len(message)))
        return message

if __name__ == '__main__':
    # Checklist
    watch_for(watchlist, searchfor, results)
    # Send email alert if item found
    if args.notify and args.username and args.passwd:
        server = "smtp.gmail.com"
        port = 587
        username = send = receive = args.username
        passwd = args.passwd
        subject = "Alert from " + os.path.basename(sys.argv[0])
        post = make_message(searchfor, results)
        alert_msg = (
                'SMTP Username + password: {} + {}\n'
                'From: {}\nTo: {}\n'
                'Subject: {}\nMessage: {}').format(
                        username, passwd, send, receive, subject, post)
        logging.debug(alert_msg)
        if len(post) != 0:
            logging.debug('Sending message ...')
            keep_me_posted(server, port, username, passwd, send, receive, 
                    subject, post)
    logging.debug('End of program')
