
'''
DONT RUN THIS , JUST FOR DEMO PURPOSES

'''


# CODEVERIFICATION
from wholemail import CodeVerificationEmailTemplate , TemplateStyles

template = CodeVerificationEmailTemplate(
					code = "12345",
					recipient_name = "JohnDoe" , 
					company_name = "WholemailApp",
					company_address = "Mars",
					customer_support_link = "support",
					company_phone_number = "+123456",
					company_website_link = "wholemailwebsite",
					company_logo_link = "Link to company logo",
					template_style = TemplateStyles.basic,
					)
# send it with the EmailWorker class or do something else



# EMAILVERIFICATION
from wholemail import  EmailVerificationEmailTemplate , TemplateStyles

template = EmailVerificationEmailTemplate(
					recipient_name = "JohnDoe" , 
					company_name = "WholemailApp",
					email_verification_link = "https://email_verify.com",
					company_address = "Mars",
					customer_support_link = "support",
					company_phone_number = "+123456",
					company_website_link = "wholemailwebsite",
					company_logo_link = "link_to_company_image_logo",
					template_style = TemplateStyles.basic
					 )
# send it with the EmailWorker class or do something else



# RESET PASSWORD

from wholemail import  ResetPasswordLinkEmailTemplate , TemplateStyles

template = ResetPasswordLinkEmailTemplate(
					reset_password_link = "password reset link",
					recipient_name = "JohnDoe" , 
					company_name = "WholemailApp",
					company_address = "Mars",
					customer_support_link = "support",
					company_phone_number = "+123456",
					company_website_link = "wholemailwebsite",
					company_logo_link = "logo link",
					template_style = TemplateStyles.basic,
					 )
# send it with the EmailWorker class or do something else



# Informative message

from wholemail import InformativeMessageEmailTemplate , TemplateStyles

# the image_links format is ->  [  [image_link , image_name], .....  ]
image_links = [
			["https://t72tank.jpg" , "t72 tank "],
			["https://puppyimage.png" , "puppy"]

		]
message = "Hello , just wrote to say this and and some images"
template = InformativeMessageEmailTemplate (
					message = message,
					title = "title of the email",
					recipient_name = "JohnDoe" , 
					image_links = image_links ,
					company_name = "WholemailApp",
					company_address = "Mars",
					customer_support_link = "support",
					company_phone_number = "+123456",
					company_website_link = "wholemailwebsite",
					company_logo_link = "https://",
					template_style = TemplateStyles.basic,
					 )
# send it with the EmailWorker class or do something else



# OFFICE LETTER TEMPLATE
from wholemail import OfficeLetterEmailTemplate ,TemplateStyles

message  = "Hello. I am writing to inform you .."
template = OfficeLetterEmailTemplate(
					message = message , 
					senders_position = "CEO", # Position the sender holds in the company 
					senders_name = "MarkZucks", # Sender;s name
					recipient_name = "JohnDoe" ,  # recipients name 
					company_name = "WholemailApp",
					company_address = "Mars",
					customer_support_link = "support",
					company_phone_number = "+123456",
					company_website_link = "wholemailwebsite",
					company_logo_link = "oursite",
					template_style = TemplateStyles.basic,
		)
# send it with the EmailWorker class or do something else


