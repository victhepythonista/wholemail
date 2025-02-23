
from wholemail import GmailSender , GmailEmailWorker

gmail_address = "mygmail@gmail.com"
gmail_app_password = "123app"

# making GmailSender object
sender = GmailSender(  gmail_address , gmail_app_password )


# making a GmailWorker object
worker = GmailEmailWorker(gmail_address, gmail_app_password )


