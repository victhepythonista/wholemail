from wholemail import BasicEmailVerificationEmailTemplate , BasicCodeVerificationEmailTemplate , TEMPLATE_STYLES_AVAILABLE

# Another way you can customize a pre-set template is by changing the style
# This is done using the prameter 'template_style:int = value'

# to see the availble template styles , do this
print(TEMPLATE_STYLES_AVAILABLE)

# lets specify the style of this pre-set template
verification_code = '123' # A code to be used for authentication/verification
verification_code_email_template = BasicCodeVerificationEmailTemplate(
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