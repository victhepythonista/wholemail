from . import base_content_paths , body_content_paths

'''

FOR GETTING EMAIL CONTENT HTML TEMPLATES 



'''

class EmailTemplateTools:
	'''
	tools to support EmailTemplate classes 

	'''
	@staticmethod
	def AddContent (email_template_class , key , new_value ):
		'''
		in the text content , the '*' symbol is used for substitution of text 
		eg...   Hello **name**  --> Hello victor  .. using the str.replace function
		'''
		key = f'**{key}**'
		cont = email_template_class.content
		if not key in cont:
			return 
		cont = cont.replace(key , new_value)
		email_template_class.content = cont 



class EmailTemplate:
	content = '' 
	base_content = ''
	body_content = '' 
	body_content_file = '' 
	base_file = ''
	def __init__(self , base_file , body_content_file ):
		self.base_file = base_file 
		self.body_content_file = body_content_file
		self.UpdateContent()

	def UpdateBaseContent (self):
		# update base  content
		data =''
		with open(self.base_file  , 'r') as f:
			data = f.read()
		self.base_content = data 

	def UpdateBodyContent(self):
		# update body content
		data =''
		with open(self.body_content_file  , 'r') as f:
			data = f.read()
		self.body_content= data 
		 
	def UpdateContent(self ):
		# add the body content  inside the  base content
		self.UpdateBaseContent()
		self.UpdateBodyContent()
		base = self.base_content
		body = self.body_content
		base = base.replace("**email_body_content**" , body )
		self.content = base

	def AddContent (self, key , new_value ):
		'''
		in the text content , the '*' symbol is used for substitution of text 
		eg...   Hello **name**  --> Hello victor  .. using the str.replace function
		'''
		key = f'**{key}**'
		cont = self.content
		if not key in cont:
			return 
		cont = cont.replace(key , new_value)
		self.content = cont 




class VerifyCodeEmailTemplate(EmailTemplate):
	'''
	keys -> [code , message , heading ]
	
	'''
	def __init__(self ):
		EmailTemplate.__init__(self , base_content_paths.verify_code  , body_content_file = body_content_paths.verify_code)
		 
	 
 


class SubjectMessageTemplate(EmailTemplate):
	'''
	keys -> [heading , message ]
	requires SUBJECT and MESSAGE only

	'''
	def __init__(self ):
		EmailTemplate.__init__(self , base_content_paths.subject_message , body_content_file = body_content_paths.subject_message)
		 
	 
 

 