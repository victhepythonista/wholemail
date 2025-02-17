
from .send_email import SendTextBasedEmail , SendHTMLEmail 
from .email_verification import RemoveEmailFromVerificationFile
from .email_verification import SignupEmailCodeVerifier, ChangeEmailAddressEmailCodeVerifier, ChangePasswordEmailCodeVerifier, RecoverPasswordEmailCodeVerifier
from .email_maker import GenerateEmail



'''

LOADING A TEMPLATE 

SENDING AN EMAIL 

VERIFYING A CODE 


'''




'''

how to send an email in views

# us the code verifier to generate a unique code
verification_code = SignupEmailCodeVerifier().NewCode(email)

#use  the GenerateEmail function to generate email_data 
	email_data = GenerateEmail.SignupEmailVerification(verification_code)
	subject = email_data['subject']
	message = email_data['message']

# send the email using the available send functions 
	SendHTMLEmail(   message , subject , [ email,])



	'''