import socket 

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText

from eqp.models import EquiplyAccount
from logging_toolkit import eqplog


GMAIL_USERNAME = "equiply.hq@gmail.com"
GMAIL_APP_PASSWORD = "anrpggjxgilailen"
 
EQUIPLY_EMAIL = GMAIL_USERNAME

FAILED_TO_SEND_MAIL_BECAUSE_OF_NETWORK = [socket.gaierror,]


def SendAnEmail(send_function , args = [] , kwargs = {} ,cache_if_fail = False  ):
	# try to send the mail and catch the falling exceptions...get it ? haha 
	# return True or False 
	try:
		send_function(*args , **kwargs )
		return True 
	except Exception as e  :
		# TODO > cache email function 
		print(f"Could not send an email SEND FUNCTION : {send_function.__name__} ... errors responsible >> {e}")
		return False 


def SendHTMLEmail( html_message , subject ,    recipients ):
	plain_message = strip_tags(html_message)
	message = EmailMultiAlternatives(
	subject = subject, 
	body = plain_message,
	from_email = EQUIPLY_EMAIL ,
	to= recipients
	)
	message.attach_alternative(html_message, "text/html")

	return SendAnEmail(message.send )
 


def SendTextBasedEmail(subject , message ,   request ,user_email  ):
	# send a text based email to the user 
	from_email = EQUIPLY_EMAIL
	recipient_list = [user_email,]
	try:
		send_mail(subject, message, from_email, recipient_list)
		return True 
	except Exception as e:
		eqplog(f"Error sending email to {user_email} using django.core.mail ... \n trying with smptserver next  ")
		return False
	# USING OTHER MEANS 
	email_text = message
	msg = MIMEText(email_text)
	msg["Subject"] = subject
	msg["To"] =  user_email
	msg["From"] = f"{GMAIL_USERNAME}"
	smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	smtp_server.login(GMAIL_USERNAME, GMAIL_APP_PASSWORD)

	send_result = SendAnEmail(smtp_server.sendmail, args = [msg["From"], recipients, msg.as_string()])
	smtp_server.quit()
	return send_result