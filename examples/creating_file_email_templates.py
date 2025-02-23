from wholemail import FileEmailTemplate

# A file email template is an email template that loads ots html content from a file
# Let's create a FileEmailTemplate object

# we have a html file 'email.html'
# the file contains the following html code :
'''
<!DOCTYPE html>
<html>
<head>
	<title>Hello {{name}}</title>
</head>
<body>

<h2>We are writing to ask for a meeting to discuss the recent quality of copper . </h2>

</body>
</html>
'''

file = "email.html"  # our html code is in this file
context = {"name":"EaNasir"}   # context that will be inserted into the html to be sent 



template = FileEmailTemplate( file , context = context , name = "complaint-email")

# NOTE : The file content will not be affected in any way , it is only read from