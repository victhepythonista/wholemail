import os 
from os.path import join 
import csv 

from logging_toolkit import eqplog
from quick_tools import WriteListToCSVFile , ReadLinesFromCSVFile
from pid_manager import Makeid

EMAIL_VERIFICATION_CODES_FOLDER = os.path.abspath('data/email_codes/')
SIGNUP_EMAIL_VERIFICATION_CODES_FILE =  join( EMAIL_VERIFICATION_CODES_FOLDER , "SIGNUP_VERIFICATION_CODES.txt")
CHANGE_EMAIL_ADDRESS_EMAIL_VERIFICATION_CODES_FILE =join(  EMAIL_VERIFICATION_CODES_FOLDER , "CHANGE_EMAIL.txt")
CHANGE_PASSWORD_EMAIL_VERIFICATION_CODES_FILE  = join( EMAIL_VERIFICATION_CODES_FOLDER , "password_change_codes.txt")
RECOVER_PASSWORD_VERIFICATION_CODES_FILE  = join( EMAIL_VERIFICATION_CODES_FOLDER, "recover_password_codes.txt")

def RemoveEmailFromVerificationFile(email , code ,file):
	# remove all rows with a matching email from the csv file 
	rows = ReadLinesFromCSVFile(file)
	clean_data = [] 
	for r in rows:
		# print(f"Trying to remove {email} {code}  from {r} \n result  -->{email == r[0]}", r)
		if len(r) !=2:continue
		if   email in r :
			continue
		clean_data.append(r)


	eqplog("REMOVED EMAIL VerificationCode INFORMATION  FROM DATA FILE ")
	WriteListToCSVFile(clean_data ,  file , overwrite = True )
	eqplog("UPDATED the data file ")


class EmailCodeVerifier:
	def __init__(self , file ):
		self.file  = file 

	def NewCode(self , email ):
		current_code_data = ReadLinesFromCSVFile(self.file)
		# print("READ DATA ", current_code_data)
		current_code_data_string = str(current_code_data)
		code = ""
		eqplog("generating an email code .. .. ")
		while code == '' or code in current_code_data_string:
			print("generating an email code for email -> ", email )
			code = Makeid(length = 6 , letters = False , numbers = True )
			if not code in current_code_data_string:
				break 
		new_row = [email , code] 
		current_code_data.append(new_row)
		WriteListToCSVFile( current_code_data, self.file) 
		eqplog(f"UPDATED NEW VERIFICATION CODE {code} TO FILE {self.file} ")
		return code 

	def IsValidCode(self , email  ,code ):
		current_code_data = ReadLinesFromCSVFile(self.file)
		for data in current_code_data:
			# print("Looking for a match "  , data )
			if len(data) != 2:
				continue
			e , c =  data 
			if e == email and c == code:
				eqplog(f"CODE [{code}] FOUND :)  \n removing to prevent code congestion .. ")
				RemoveEmailFromVerificationFile( e , c  , self.file)
				return True 
		return False

	def GetCode(self,user_email) -> str:
		'''
		For testing purposes. 
		Get the code sent tok and email 
		'''
		file_rows = ReadLinesFromCSVFile(self.file)
		code = ""
		for row in file_rows:
			if not len(row) == 2:
				continue
			email ,code = row
			if email ==user_email :
				return code
		return ""

 
class SignupEmailCodeVerifier(EmailCodeVerifier):

	def __init__(self ):
		EmailCodeVerifier.__init__(self ,SIGNUP_EMAIL_VERIFICATION_CODES_FILE )

class ChangeEmailAddressEmailCodeVerifier(EmailCodeVerifier):

	def __init__(self ):
		EmailCodeVerifier.__init__(self ,CHANGE_EMAIL_ADDRESS_EMAIL_VERIFICATION_CODES_FILE )



class ChangePasswordEmailCodeVerifier(EmailCodeVerifier):

	def __init__(self ):
		EmailCodeVerifier.__init__(self ,CHANGE_PASSWORD_EMAIL_VERIFICATION_CODES_FILE )




class RecoverPasswordEmailCodeVerifier(EmailCodeVerifier):

	def __init__(self ):
		EmailCodeVerifier.__init__(self ,RECOVER_PASSWORD_VERIFICATION_CODES_FILE)
