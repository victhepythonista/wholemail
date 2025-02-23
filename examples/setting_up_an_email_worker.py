from wholemail import GmailEmailWorker , EmailCodeVerifier , EmailTemplate

# In this demonstration  ,  we will use the GmailEmailWorker
storage_folder = "data/"
my_email = "myemail@gmail.com"
email_password = "dfujsdfv"

# initialize the worker object
worker = GmailEmailWorker(my_email , email_password , storage_folder = storage_folder)
 
# To send a template you just do this 
# Create an email template
html = "<h1>Hello   {{name}}</h1>" # our html code in text form
context = {"name":"EaNasir"} # context that will be inserted into the html
template_name  = "hello-template"
template = EmailTemplate( html , context = context , name = template_name)
# Prepare the recipient information
subject = "Saying hello" # subject of the email
recipient_email = "recipient@gmail.com" # the email of the receiver

# send the template 
worker.SendTemplate( template , subject , recipient_email )





