
from wholemail import GmailEmailWorker , EmailCodeVerifier , BasicCodeVerificationEmailTemplate

# This is a demonstration of how to verify codes using the EmailWorker class
# We will use the GmailWorkerClass for this demo

my_email = "myemail@gmail.com"
gmail_app_password = "dfujsdfv"
storage_folder = "data/"

# recipient information
subject = "Verification" # subject of the email
recipient_email = "recipient@gmail.com" # the email of the receiver

# initialize the worker object
worker = GmailEmailWorker(my_email , gmail_app_password , storage_folder = storage_folder)

# Let us now create a code verifier and dictate ho we want the code to look like
file = "store_codes_here.txt" # where to store the codes
verifier = EmailCodeVerifier( 
				file ,
				length = 5 , # length of the code to be generated
				numbers = True , # to include numbers or not
				letters = True , # to include alphabetical letters or not
				punctuation_chars = True , # to include punctuation charachters or not
				casing = "upper" # Casing to use , you can choose between - upper , lower , all , the default is upper
						 )
# Let's generate a code we will send to the user
code = verifier.MakeNewCode(recipient_email)


# create and add the preset template made for code verification
template = BasicCodeVerificationEmailTemplate(
					code , # A code to be used for authentication
					'JaneDoe', # reciients name
					company_name = "Company Inc", # comapny name
					company_address = "earth", # address
					customer_support_link = "company.com/company_support" , # url for customer support
					company_phone_number = "+3436536", # company phone number
					company_website_link = "company.com", # company website url
					name = "verification-template", # name of the template , optional

				)
# send the Email with the verification code information
worker.SendTemplate( template , subject , recipient_email )

# verify the code
is_valid_code = worker.VerifyCode(code)

# do something with the result





