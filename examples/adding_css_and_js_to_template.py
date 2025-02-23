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
