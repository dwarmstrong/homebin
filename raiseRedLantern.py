"""A set of classes to add notification capabilities to scripts."""

import logging, re, smtplib

class MakeMessage():
    """Generate a notification message."""
    
    def __init__(self, trigger_event_regex, to_be_reported):
        """Initialize attributes."""
        self.trigger_event_regex = trigger_event_regex
        self.to_be_reported = to_be_reported

    def trigger_message(self):
        """Events that require notification."""
        with open(self.to_be_reported, 'r') as f:
            message = ""
            report = f.readlines()
            logging.debug('== Results ==\n{}\n'.format(report))
            regex = re.compile(r'.*({}).*'.format(self.trigger_event_regex))
            ## If the trigger event regex shows up anywhere in the report, 
            ## return a message containing the report contents
            if any(regex.search(line) for line in report):
                for line in report:
                    message += line
            logging.debug('Message length: {}'.format(len(message)))
            return message


class EmailAlert():
    """Notify recipient via email"""

    def __init__(self, smtp_server, port, acct_username, acct_password, 
            sent_from, recipient, subject, message):
        """Initialize attributes."""
        self.smtp_server = smtp_server
        self.port = port
        self.acct_username = acct_username
        self.acct_password = acct_password
        self.sent_from = sent_from
        self.recipient = recipient
        self.subject = subject
        self.message = message

    def notify_by_mail(self):
        """Configure SMTP details and send message."""
        ## Connect to host
        try:
            server = smtplib.SMTP(self.smtp_server, self.port)
        except smtplib.socket.gaierror:
            return false
        server.ehlo()
        server.starttls()
        ## Login
        try:
            server.login(self.acct_username, self.acct_password)
        except SMTPAuthenticationError:
            server.quit()
            return False
        ## Send message
        msg = "Subject: " + self.subject + "\n" + self.message
        try:
            server.sendmail(self.sent_from, self.recipient, msg)
            return True
        except Exception:
            return False
        finally:
            server.quit()
