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