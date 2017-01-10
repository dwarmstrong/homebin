#!/usr/bin/env python3

import argparse, logging, os, sys
from os.path import expanduser

from bernersLee import CheckList
from raiseRedLantern import EmailAlert, MakeMessage

logging.basicConfig(level=logging.DEBUG, 
                format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program')

msg = """
(O< .: Check to see if Toronto Public Library has added an item to catalogue.
(/)_
"""

parser = argparse.ArgumentParser(description=msg,
    formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-n", "--notify", 
    help="email notification", action="store_true")
parser.add_argument("-i", "--id", 
    help="config file with SMTP username and password")
parser.add_argument("-u", "--username", help="SMTP username")
parser.add_argument("-p", "--passwd", help="SMTP password")
args = parser.parse_args()

home = expanduser("~")
watchlist = home + "/doc/log/tplWatch"
searchfor = "total-results"
results = home + "/doc/log/tplMatch" 
mail_id = home + "/.mail_id"

def main():
    ## Checklist
    tpl = CheckList(watchlist, searchfor, results)
    tpl.check_for()
    ## Send email alert if item found
    email_message = MakeMessage(searchfor, results)
    post = email_message.trigger_message()
    if len(post) != 0:
        server = "smtp.gmail.com"
        port = 587
        tpl_alert = EmailAlert(server, port)
        if args.notify and args.username and args.passwd:
            user = send = receive = args.username
            passwd = args.passwd
        elif args.notify and args.id:
            ident = tpl_alert.user_pass_config(mail_id)
            user = send = receive = ident[0]
            passwd = ident[1]
        else:
            print("Note: Require a SMTP user:passwd to send email alert.")
            sys.exit()
        subject = "Alert from " + os.path.basename(sys.argv[0])
        alert_msg = ('Server: {}\nPort: {}\n'
            'SMTP username: {}\nSMTP password: {}\n'
            'From: {}\nTo: {}\nSubject: {}\n'
            'Message: {}').format(server, port, user, passwd, send, receive, 
                subject, post)
        logging.debug(alert_msg)
        tpl_alert.notify_by_mail(user, passwd, send, receive, subject, post)
        logging.debug('Message sent.')

if __name__ == '__main__':
    main()
    logging.debug('End of program')
