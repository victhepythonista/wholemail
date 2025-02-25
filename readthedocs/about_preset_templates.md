# PRESET  TEMPLATES

- Preset templates are built with the main purpose of allowing for quick  deployment and sending of generic emails . An example is a OTP(One Time Password) email which is very common .
- They all are children classes of the ***FileEmailTemplate*** class which itself is a child class of **EmailTemplate** 
- Check out the   <a href="https://github.com/victhepythonista/wholemail/blob/main/wholemail/email_template.py" target="_blank">source code </a>  
- Here are   <a href="https://github.com/victhepythonista/wholemail/blob/main/readthedocs/all_templates_screenshots" target="_blank">  screenshots </a> of all email templates supported

- These are the current available preset email templates classes :

	- EmailVerificationEmailTemplate
	- CodeVerificationEmailTemplate
	- ResetPasswordLinkEmailTemplate
	- InformativeMessageEmailTemplate
	- OfficeLetterEmailTemplate
	
- More templates on the way ,  <a href="https://github.com/victhepythonista/wholemail/blob/main/CONTRIBUTE_A_TEMPLATE.md" target="_blank">  see how you can contribute a template .</a>
--------



##  EmailVerificationEmailTemplate

- This is used to send links used for account verification 
- Here is a <a href="https://github.com/victhepythonista/wholemail/blob/main/screenshots/email_templates/email_verification_style1.png" target="_blank">  screenshot </a> of an email sent using this class
- Here is how to initialize it 


```python
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
```

## CodeVerificationEmailTemplate

- This template is used to send One Time Password type of emails
-  Here is a <a href="https://github.com/victhepythonista/wholemail/blob/main/screenshots/email_templates/verification_code_style1.png" target="_blank">  screenshot </a> of an email sent using this class
- You can generate your code or OTP elsewhere and add it during initialization like so :

```python
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
```
## ResetPasswordLinkEmailTemplate


- This template is used to send a url  with which a user can follow to reset their account password 
- This is a pretty common email
-  Here is a <a href="https://github.com/victhepythonista/wholemail/blob/main/screenshots/email_templates/reset_password_style1.png" target="_blank">  screenshot </a> of an email sent using this template
- Initialize the class like so :

```python
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


```



##  InformativeMessageEmailTemplate

- This is a template used to send an email that is made of images  along with a text message 
- The format will be :
			-  TITLE
			-  IMAGES
			- MESSAGGE
			- FOOTER
-  Here are  <a href="https://github.com/victhepythonista/wholemail/blob/main/screenshots/email_templates/informative_message_style1_partA.png" target="_blank">  screenshotA </a> and  <a href="https://github.com/victhepythonista/wholemail/blob/main/screenshots/email_templates/informative_message_style1_partB.png" target="_blank">  screenshot B</a> of an email sent using this template
- Initialize it like so 

```python
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


```


## OfficeLetterEmailTemplate

- This class is for sending generic office letter type emails . 
- Such emails start off with a greeting , then a text body and finally the sign off text 
-   Here is a <a href="https://github.com/victhepythonista/wholemail/blob/main/screenshots/email_templates/office_letter_style1.png" target="_blank">  screenshot </a> of an email sent using this template
- Initialize it like so 


```python
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


```
