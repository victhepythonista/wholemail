# This is a demonstration of using wholemail in djnago

from django.http import HttpResponse , HttpRequest 

from wholemail import GmailSender

password , email = "123" , "myemail@domain.com"
sender = GmailSender(email , password)
html = '<h1>Hello</h1>'

# sending a text email in a view
def SendHelloEmail(request):
	user_email = "JohnDoe@domain"
	subject ="Subject is saying hi"
	message = "hi"
	sender.SendTextEmail(user_email , subject, message)
	# continue with yur code

# sending a html email
def SendHtmlEmailToUser(request):
	user_email = "JohnDoe@domain"
	subject ="Subject is this is html"
	message = "Alternative message"
	sender.SendHTMLEmail(user_email , subject,html , plain_message =  message)
	# continue with yur code
