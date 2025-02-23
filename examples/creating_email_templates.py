from wholemail import EmailTemplate

# the EmailTemplate class can be sent via an EmailWorker class
# They simply represent the email you want to send
# Let's create a simple email template 

html = "<h1>Hello   {{name}}</h1>" # our html code in text form
context = {"name":"EaNasir"} # context that will be inserted into the html

template = EmailTemplate( html , context = context , name = "hello-email")