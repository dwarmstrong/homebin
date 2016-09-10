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

    def __init__(self, smtp_server, port):
        """Initialize attributes."""
        self.smtp_server = smtp_server
        self.port = port

    def user_pass_config(self, mail_config):
        """Add email username and password to list."""
        with open(mail_config, 'r') as f:
            ident = [line.strip() for line in f]
            return ident

    def notify_by_mail(self, username, password, sent_from, recipient, 
        subject, message):
        """Configure SMTP details and send message."""
        ## Connect to host
        try:
            server = smtplib.SMTP(self.smtp_server, self.port)
        except smtplib.socket.gaierror:
            return false
        server.ehlo()
        server.starttls() # after connecting ... upgrade to TLS
        ## Login
        try:
            server.login(username, password)
        except SMTPAuthenticationError:
            server.quit()
            return False
        ## Send message
        msg = "Subject: " + subject + "\n" + message
        try:
            server.sendmail(sent_from, recipient, msg)
            return True
        except Exception:
            return False
        finally:
            server.quit()
