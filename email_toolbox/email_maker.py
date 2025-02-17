from .email_templates import VerifyCodeEmailTemplate , SubjectMessageTemplate , EmailTemplateTools



class GenerateEmail:
	' creates html based emails from the required parameters '
	''
	@staticmethod
	def SignupEmailVerification( code  ):
		subject = "Verify your email address "
		message = f"""
Use the code below to complete sign up 
		"""
		
		template = VerifyCodeEmailTemplate()
		template.AddContent('subject' , subject)
		template.AddContent('message' , message)
		template.AddContent('code' , code)
		return {
			'message':template.content ,
			'subject':subject,
		}

	@staticmethod
	def EmailChange(code , user ):
		'changing an email address'
		message = """
		HELLO  %s. 
		changing your Equiply email to this one ?

		Well heres the code below: """ 
		subject = "Change email address "
		template = VerifyCodeEmailTemplate()
		template.AddContent('subject' , subject)
		template.AddContent('message' , message)
		template.AddContent('code' , code)
		return {
			'message':template.content ,
			'subject':subject,
		}


	@staticmethod
	def PasswordChangeVerifyWithCode(code , user ):
		'changin password but must confirm identity with email'
		message = """
		HELLO  %s. 
		changing your password? Use this code 

			CODE : %s

		If this is not you can safely ignore this email . """%(user.username , code )
		subject = "Confirm password reset "
		template = VerifyCodeEmailTemplate()
		template.AddContent('subject' , subject)
		template.AddContent('message' , message)
		template.AddContent('code' , code)
		return {
			'message':template.content ,
			'subject':subject,
		}
	@staticmethod
	def RecoverPassword(code , user ):
		'changin password but must confirm identity with email'
		message = """
		HELLO  %s. 
		If you are trying to recover your password, use the code below  

			CODE : %s

		If this is not you can safely ignore this email . """%(user.username , code )
		subject = "Confirm password reset "
		template = VerifyCodeEmailTemplate()
		template.AddContent('subject' , subject)
		template.AddContent('message' , message)
		template.AddContent('code' , code)
		return {
			'message':template.content ,
			'subject':subject,
		}
	 