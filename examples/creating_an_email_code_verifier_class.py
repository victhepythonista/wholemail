
from wholemail import EmailCodeVerifier


# The EmailCodeVerifier class is used to generate unique authentication codes ,
# which are stored in files
# This class is used by the EmailWorker class to validate and generate codes 
# It  alllows you to modify code generation

file = "store_codes_here.txt" # where to store the codes
verifier = EmailCodeVerifier( 
				"My code verifier",
				file ,
				length = 5 , # length of the code to be generated
				numbers = True , # to include numbers or not
				letters = True , # to include alphabetical letters or not
				punctuation_chars = True , # to include punctuation charachters or not
				casing = "upper" # Casing to use , you can choose between - upper , lower , all , the default is upper
				 )


# You can clear the codes file using the method ClearCodes
# like this :
verifier.ClearCodes()
# the file is now emptys