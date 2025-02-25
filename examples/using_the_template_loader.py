from wholemail import LoadTemplate


# Lets create an email template class using the LoadTEmp
# load from a file
context = {"name":"Jane"}
template = LoadTemplate( html_file = "myfile.html"  ,context = context)

# load from text 
template = LoadTemplate(html_text = "<h1> {{name}} </h1>" ,context = context)