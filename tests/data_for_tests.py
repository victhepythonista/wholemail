
from wholemail  import EmailTemplate, EmailCodeVerifier


test_html_text = """
<h2>
{{name}} ( born Albert Chinụalụmọgụ Achebe; {{DOB}} – 21 March 2013)
 was a Nigerian novelist, poet, and critic who is regarded as a central figure of modern African literature.
  His first novel and magnum opus, Things Fall Apart (1958), occupies a pivotal place in African literature and
   remains the most widely studied, translated, and read African novel.

    Along with Things Fall Apart, his No Longer at Ease (1960) and Arrow of God (1964) complete the "African Trilogy".
     Later novels include A Man of the People (1966) and Anthills of the Savannah (1987).
      Achebe is often referred to as the "father of modern African literature",
      although he vigorously rejected the characterization.
</h2>
     """
test_context = {
	"name":"Chinua Achebe",
	"DOB":"16 November 1930",
}
test_html_file = "test_data/html/chinua_achebe.html"
test_email_template = EmailTemplate(test_html_text,test_context)

test_code_verifiers = {
	"auth":EmailCodeVerifier("auth_verifier" , "test_data/test_email_codes.txt"),
}