

 
<p align="center">
    <img width=120 height=120 src="https://i.ibb.co/q3tdgSsM/wholemail-new-logo.png" > </img>
 
</p>


<div align="center">
<a href="https://www.python.org/"><img height=30  src="https://img.shields.io/badge/built%20with-Python3-blue.svg" alt="built with Python3"></a>
		<a href="https://pepy.tech/projects/wholemail"><img height=30 src="https://static.pepy.tech/badge/wholemail" alt="PyPI">
<a href="https://github.com/victhepythonista/wholemail"><img height=30   src="https://img.shields.io/github/stars/victhepythonista/wholemail.svg?style=social&label=Stars"></a>
</div>





# Introduction



-  Wholemail is a lucid Python package built to facilitate easy sending of emails and other common generic functionality like sending authentication code emails .
- Jinja2 is used to render the HTML code , so that means you can add your own Jinja2 expressions and blocks like in the example below :





```python
from wholemail import LoadTemplate , GmailWorker

worker = GmailWorker("mygmail@gmail.com" , "gmail_app_password") # will send the email
html_text = """
	
	{%if won_the_prize %}

		<h3>{{name}} , you won ! we'll contact you</h3>

	{%else%}
		<p>Better luck next time</p>
	{%endif%}

"""
context = {
	
	"name":"JaneDoe",
	"won_the_prize":True,
}

template = LoadTemplate(html_text = html_text , context = context )


recipient  ,subject = "recipient@gmail.com" , "The prize"
# send the template 
worker.SendTemplate( template , subject ,recipient)



```

### An example of preset email templates for you to choose from
 
 
Office letter template     |  Verificaton code template
:-------------------------:|:-------------------------:
![Office letter email example](https://github.com/victhepythonista/wholemail/blob/main/screenshots/email_templates/office_letter_style_1.png)  |  ![Vericfication code email example](https://github.com/victhepythonista/wholemail/blob/main/screenshots/email_templates/verification_code_style1.png)
 

----
###


#### Main features 


 - Easily send text-based and HTML emails
 - ***Jinja2*** expressions and blocks in your HTML code will be automatically rendered and processed
- Preset email templates lighten your load when you need to send for common generic emails . eg OTP email
- Create , customize and send your own email templates
- Saves you the hustle of writing email sending functions


##
- Check out the <a href="https://github.com/victhepythonista/wholemail/blob/main/RELEASE_NOTES.md" target="_blank"> release notes</a>  to stay updated on recent changes and contributions
-    More HTML templates needed , you are welcome to <a href="https://github.com/victhepythonista/wholemail/blob/main/CONTRIBUTE_A_TEMPLATE.md" target="_blank"> contribute a new HTML template  </a>  
 -   <a href="https://github.com/victhepythonista/wholemail/blob/main/CONTRIBUTE.md" target="_blank">Contributions </a> and ideas are welcome , and for Pete's sake , help me write better code .
- More templates on the way  
- Here are   <a href="https://github.com/victhepythonista/wholemail/blob/main/readthedocs/all_templates_screenshots.md" target="_blank">  screenshots </a>  of all the   <a href="https://github.com/victhepythonista/wholemail/blob/main/readthedocs/about_preset_templates.md" target="_blank">    preset templates  </a>for you to choose from




 ## **TAKE NOTE** :

 #### Before using with gmail
 
 - If you want to send emails via gmail, make sure you <a href="https://github.com/victhepythonista/wholemail/blob/main/help/creating_gmail_app_passwords.md" target="_blank"> set up your Gmail APP PASSWORD </a> ,  otherwise using your *NORMAL*  Gmail password WILL NOT work  since  Google disabled less secure apps
 - Read more about GMAIL <a href="https://support.google.com/accounts/answer/6010255?hl=en" target="_blank">  less secure apps </a>
 

 After setting up your password you can use it like so 


 ```python
 
from wholemail import GmailSender , GmailEmailWorker

gmail_address = "mygmail@gmail.com"
gmail_app_password = "123app"

# making GmailSender object
sender = GmailSender(  gmail_address , gmail_app_password )


# making a GmailWorker object
worker = GmailEmailWorker(gmail_address, gmail_app_password )



 ```


---------




 

# Getting started

### Installation

##### Windows OS installation using pip

```
python3 -m pip install wholemail

```

alternatively 

```
pip install wholemail
```

or

```
py -m pip install wholemail
```

To upgrade your version in Windows ,just use the --upgrade  option when installing . Like so :

```
python -m pip install --upgrade wholemail
```

### Dependencies

-  <a href="https://jinja.palletsprojects.com/en/stable/intro/#installation" target="_blank">Jinja2</a>
-  <a href="https://pypi.org/project/code-monger/" target="_blank"> code-monger</a>
- smptlib - Comes with the Python Standard Library
- bs4 - <a href="https://pypi.org/project/beautifulsoup4/" target="_blank">Beautiful soup</a> 

### Supported emails

- Support for more email providers is on the way 


- [x] Gmail
- [ ] Yahoo
- [ ] Proton mail
- [ ] Outlook



# Usage

#### Contents

-  Sending emails via GMAIL
- Using the **LoadTemplate** function
-    Working with the EmailTemplate class 
- Working with the EmailWorker class
- Sending a generic email verification email
 - Sending a generic authentication code email
 - Using the  EmailWorker to authenticate codes
 - Using in a Django view
 - Adding Javascript and CSS code to the HTML of an EmailTemplate class
 - Changing preset email styles


--- 

### Sending emails via GMAIL

 

- You can send html and plain text messages using the EmailSender class
- Here is a demonstration





```python

from wholemail import GmailSender

# to send a gmail email you can use the GmailSender class
sender = GmailSender(  "mygmail@gmail.com" , "password" )

# To send a simple text based message , use the SendTextMail method like so
recipient = "recipient@gmail.com" # recipients email address
message = "Hey there pal" # message to send
subject = "saying hello" # email subject

sender.SendTextMail( recipient , subject , message )# This will send an email to the recipient with the provided message


# to send a html message
html_code = "<h1>Hello  there pal</h1>" # html to send
subject = "saying hi" #  Subject of the email
plain_message = "Hello there" # alternative message to the html , it is optional

sender.SendHTMLEmail( recipient , subject ,html_code , plain_message = plain_message )
# This will send an html email to the recipient

```


### Using the LoadTemplate function

- One way to ceate  an **EmailTemplate** is by using the **LoadTemplate** function


```python
from wholemail import LoadTemplate


# Lets create an email template class using the LoadTEmp
# load from a file
context = {"name":"Jane"}
template = LoadTemplate( html_file = "myfile.html"  ,context = context)

# load from text 
template = LoadTemplate(html_text = "<h1> {{name}} </h1>" ,context = context)
```



### Working with the EmailTemplate class
 

- The EmailTemplate class represents the email you wish to send .
- It contains the text message or html code that will make up the email . 
- Most importantly , it allows for customization . ie . You can add custom content and context 
- You can also create a template using the **LoadTemplate** function
- Below is a demonstration is creating an EmailTemplate class :






```python
from wholemail import EmailTemplate

# the EmailTemplate class can be sent via an EmailWorker class
# They simply represent the email you want to send
# Let's create a simple email template 

html = "<h1>Hello   {{name}}</h1>" # our html code in text form
context = {"name":"EaNasir"} # context that will be inserted into the html

template = EmailTemplate( html , context = context , name = "hello-email")
```

---



### Working with the EmailWorker class
 

- The EmailWorker class is primarily  used to send email templates and verify email codes 





```python
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
```

---


### Sending a generic email verification email
 

- Email verification through a link sent to your email is a common practice across the web.
- The **EmailVerificationEmailTemplate** is an child of the EmailTemplate class that is made to simplify this common practice of verifying emails .
- Below is an example of loading the template
- Check out all preset templates here






```python
from wholemail import EmailVerificationEmailTemplate

# Pre-set templates like EmailVerificationEmailTemplate make work easier when you want
# to send emails that involve the user clicking a link for verification purposes
# All you need is to provide some parameters and you are good to go
# EmailVerificationEmailTemplate is used to send an email with a link for the user 
# to click and verify their identity doing so 
# The common details like the verification link , company info , company address etc can be easily inserted,
# saving you the hustle

verification_link = "https://company.com/verification" # The link the user will click to verify their email
company_name = "Samsung"
recipient_name 	= "Mark"
email_verification_template = EmailVerificationEmailTemplate(
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
``` 

---



###  Sending a generic authentication code email

 

- Another common email is the verification code or one-time-password (OTP) email 
- They are mostly used to authenticate an action on a website or a sign up process
- The **CodeVerificationEmailTemplate** class was built to make sending verification code emails much easier
- Here is an example of loading and sending the template

```python
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
```



---



### Using the  EmailWorker to authenticate codes

 

- If you wish to generate and authenticate codes sent to user emails , the EmailWorker class can be used to do so.
- Here is an example





```python

from wholemail import GmailEmailWorker , EmailCodeVerifier , CodeVerificationEmailTemplate

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
template = CodeVerificationEmailTemplate(
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
```


---


### Using in a Django view


- If you use the Django framework, here is an example of using the wholemail library in a view .



```python
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
```

---




### Adding Javascript and CSS code to the HTML of an EmailTemplate class

- If you can't write your Javascript and CSS in a html file and load it with a FileEmailTemplate , you can try using this method .



```python
from wholemail import  FileEmailTemplate , EmailTemplate

# If you require Javascript or CSS code in your EmailTemplate , 
# you can simply add it in the context of an EmailTemplate

html_file = "myhtml.html"
# html file contents
'''

<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
<style>
	{{my_style}}
</style>
<script>
	{{my_javasscript}}
</script>
</body>
</html>

'''

javascript_code = 'function(){alert("Hello")}'
css_code = "body{color:black;}"
context = {
	"my_style":css_code,
	"my_javasscript":javascript_code,
}

# using the  FileEmailTemplate class
template = FileEmailTemplate(  html_file , context )

# using the EmailTemplate class
context = {"css":css_code , "js":javascript_code}
html_code = """<!DOCTYPE html>
<html><head>	<title></title>
</head><body>
<style>
	{{css_code}}
</style>
<script>
	{{js}}
</script>
</body>
</html>"""
template  = EmailTemplate( html_code , context  )


# just like that, the HTML will have the required extra code 

```


---


### Changing preset email styles


- The preset email templates can be customized by using the **template_style** key word argument.
- This only works on preset templates , ***not*** **FileEmailTemplate** or **EmailTemplate**
- Here is an example :




```python
from wholemail import EmailVerificationEmailTemplate , CodeVerificationEmailTemplate , TEMPLATE_STYLES_AVAILABLE

# Another way you can customize a pre-set template is by changing the style
# This is done using the prameter 'template_style:int = value'

# to see the availble template styles , do this
print(TEMPLATE_STYLES_AVAILABLE)

# lets specify the style of this pre-set template
verification_code = '123' # A code to be used for authentication/verification
verification_code_email_template = CodeVerificationEmailTemplate(
					verification_code ,
					'JaneDoe', # reciients name
					company_name = "Company Inc", # comapny name
					company_address = "earth", # address
					customer_support_link = "company.com/company_support" , # url for customer support
					company_phone_number = "+3436536", # company phone number
					company_website_link = "company.com", # company website url
					template_style = 1 , 
				)
# note that  we specified 'template_style=1'
# Make sure the number represents a valid style 
```



# The End


- I wish you a fantastic time , thank you for checking this out . More is on the way . Thank you .   
 # **: )**
