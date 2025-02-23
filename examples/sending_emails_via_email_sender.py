
from wholemail import GmailSender

# to send a gmail email you can use the GmailSender class
sender = GmailSender(  "mygmail@gmail.com" , "password" )

# To send a simple text based message , use the SendTextMail method like so
recipient = "recipient@gmail.com" # recipients email address
message = "Hey there pal" # message to send
subject = "saying hello" # email subject

sender.SendTextMail( recipient , subject , message )# This will send an email to the recipient with the provided message


# to send a html message
html_code = "<h1>Hello  there pal</h1>" # html to send
subject = "saying hi" #  Subject of the email
plain_message = "Hello there" # alternative message to the html , it is optional

sender.SendHTMLEmail( recipient , subject ,html_code , plain_message = plain_message )
# This will send an html email to the recipient