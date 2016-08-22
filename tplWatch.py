#!/usr/bin/env python3

import argparse, logging, os, sys
from os.path import expanduser

from bernersLee import CheckList
from raiseRedLantern import EmailAlert, MakeMessage

logging.basicConfig(level=logging.DEBUG, 
                format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
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

def main():
    ## Checklist
    tpl = CheckList(watchlist, searchfor, results)
    tpl.check_for()
    ## Send email alert if item found
    if args.notify and args.username and args.passwd:
        server = "smtp.gmail.com"
        port = 587
        username = send = receive = args.username
        passwd = args.passwd
        subject = "Alert from " + os.path.basename(sys.argv[0])
        email_message = MakeMessage(searchfor, results)
        post = email_message.trigger_message()
        alert_msg = (
                'SMTP Username + password: {} + {}\n'
                'From: {}\nTo: {}\n'
                'Subject: {}\nMessage: {}').format(
                        username, passwd, send, receive, subject, post)
        logging.debug(alert_msg)
        if len(post) != 0:
            logging.debug('Sending message ...')
            tpl_alert = EmailAlert(server, port, username, passwd, send, 
                    receive, subject, post)
            tpl_alert.notify_by_mail()


if __name__ == '__main__':
    main()
    logging.debug('End of program')
