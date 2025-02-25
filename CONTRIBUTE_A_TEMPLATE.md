
## How to contriubte a template




# Steps to follow when contributing a template

- Create a class in the email_template.py class that inherits from PresetEmailTemplate
- Make sure  the class name  ends with 'EmailTemplate' ( for practicality and namespacing )
- Create files named **INSERT_STYLE_NAME**.html in all the folders in the folder **wholemail/html_boilerplates** folder 
- Edit the **template_styles.py**  and **pre_set_email_templates.py** too and add the template information as required . 
- Edit the  **__init__.py** file and import the class from there and include it in the **__all__** list 
- Send yourself  this template using the **EmailWorker** or the **EmailSender**and take screenshots 
- Add the screenshots to **screenshots/email_templates/** folder
- Edit the **readthedocs/about_preset_templates.md** and **readthedocs/all_templates_screenshots.md** and add necessary information and image links regarding the template 
- Make sure to provide adequate documentation where necessary
- Create a pull request




### If you don't know Python , but know HTML

- Create your html files , include the CSS and JS into that one html file
- Test and make sure everthing works on your end 
- Reach out to a contributor and they will do the necessary to integrate your template. 
