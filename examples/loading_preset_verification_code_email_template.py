from wholemail import CodeVerificationEmailTemplate

# Pre-set templates like EmailVerificationEmailTemplate make work easier when you want
# to send common emails 
# All you need is to provide some parameters and you are good to go

# CodeVerificationEmailTemplate is used to send an email with a code to be
# used by the recipient for authentication purposes
# This type of email is very common

verification_code = '123' # A code to be used for authentication/verification

verification_code_email_template = CodeVerificationEmailTemplate(
					verification_code ,
					'JaneDoe', # reciients name
					company_name = "Company Inc", # comapny name
					company_address = "earth", # address
					customer_support_link = "company.com/company_support" , # url for customer support
					company_phone_number = "+3436536", # company phone number
					company_website_link = "company.com", # company website url

				)
# Proceed to send the template using an EmailWorker class of your choice
my_email = "myemail@gmail.com"
email_password = "dfujsdfv"
storage_folder = "data/"

#Lets use the GmailEmailWorker to send this email template
# initialize the worker object
worker = GmailEmailWorker(my_email , email_password , storage_folder = storage_folder)
worker.SendTemplate( template , "Email subject "  , "recipient@gmail.com")