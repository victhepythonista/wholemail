from wholemail import BasicEmailVerificationEmailTemplate

# Pre-set templates like BasicEmailVerificationEmailTemplate make work easier when you want
# to send emails that involve the user clicking a link for verification purposes
# All you need is to provide some parameters and you are good to go
# BasicEmailVerificationEmailTemplate is used to send an email with a link for the user 
# to click and verify their identity doing so 
# The common details like the verification link , company info , company address etc can be easily inserted,
# saving you the hustle

verification_link = "https://company.com/verification" # The link the user will click to verify their email
company_name = "Samsung"
recipient_name 	= "Mark"
email_verification_template = BasicEmailVerificationEmailTemplate(
					recipient_name ,  # name of the recipient
					company_name, # company name
					verification_link , # The link for verification
					company_address = "Albuquerque", # address
					customer_support_link = "companysupport.com" , # a url for customer support
					company_phone_number = "+1234567", # company phone number +123
					company_website_link = "company.com", # company website url

					)

# Proceed to send the template using an EmailWorker class of your choice
my_email = "myemail@gmail.com"
email_password = "dfujsdfv"
storage_folder = "data/"

#Lets use the GmailEmailWorker to send this email template
# initialize the worker object
worker = GmailEmailWorker(my_email , email_password , storage_folder = storage_folder)
# send the email template
worker.SendTemplate( template , "Email subject "  , "recipient@gmail.com")