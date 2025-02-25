




### Steps to follow when contributing a PesetEmailTemplate class

- Clone this repo
- Go to **pre_set_email_templates.py** and add the paths to your new template class files 
 Example : 

 ```python
MY_NEW_TYPE_OF_GENERIC_TEMPLATES = {
	
	1:path_to_html_file_of_style_1,
		2:path_to_html_file_of_style_2,

	
}



 
 ```

The paths to the html files above  should be in the directory **wholemail/html_boilerplates/INSERT_TEMPLATE_CLASS_NAME**
AND **MUST** be of the expected theme . ie in the folder **email_verification** we have files "basic.html" , "japanese_indigo.html" ....use this format and copy their html code and use their themes to create your template . 
The html files must contain valid jinja variable blocks that reflect with the needed class parameters . eg {{city}}  in the html file matches the parameter 'city='New York' in the __init__ function of your class 
It's painstaking at first but easy as you go on 

- In **email_template.py** create a  class that inherits from PresetEmailTemplate
- Make sure  the class name  ends with 'EmailTemplate' ( for practicality and namespacing )
- Make sure to include this part during initialization


```python
html_file = pre_set_email_templates.YOUR_TEMPLATE[template_style]
		PresetEmailTemplate.__init__(self, html_file , name = "Preset-code-verification-template")
		insert_context_into_preset_class_during_init(self , locals())
```
 
- Edit the  **pre_set_email_templates.py** too and add the template information as required . 
- Edit the  **__init__.py** file and import the class from there and include it in the **__all__** list 
- Send yourself  this template using the **EmailWorker** or the **EmailSender**and take screenshots 
- Add the screenshots to **screenshots/email_templates/** folder
- Edit the **readthedocs/about_preset_templates.md** and **readthedocs/all_templates_screenshots.md** and add necessary information and image links regarding the template 
- Make sure to provide adequate documentation where necessary
- Do necessary tests , write necessary tests 
- Create a pull request




 -----


### Contributing a template style

- Clone this repo
- Have your html file ready (should be one file with all the styling and js)
- In the folder **wholemail/html_boilerplates** , under every folder, create an html file , paste your code and edit the code to have the required template expressions and blocks  ie {{ variable}}    
- Edit the **template_styles.py**  and **pre_set_email_templates.py** and add the required template style information



------

### If you don't know Python , but know HTML , you can contribute a template style like so :

- Create your html files , include the CSS and JS into that one html file
- Test and make sure everthing works on your end 
- Reach out to a contributor with the html file and your template style name  and they will do the necessary to integrate your template. 
