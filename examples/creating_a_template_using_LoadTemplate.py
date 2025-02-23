
from wholemail import LoadTemplate

# An alternative way of creating an EmailTemplate object is by using the LoadTemplate function
# You can provide the html code as a string or file path or both 

# creating an EmailTemplate object from a string
context = {"name":"JohnDoe"} # the information to be inserted into the html
html_text = "<h4> Hello there {{name}} </h4>"
template = LoadTemplate ( html_text = html_text , context = context , name = "says-hello")  

# creating an EmailTemplate object from a file
html_file = "hello.html"
template = LoadTemplate( html_file = html_file , context = context , name = "say-hello")
