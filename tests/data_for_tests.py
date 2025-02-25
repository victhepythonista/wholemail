
from wholemail  import EmailTemplate, EmailCodeVerifier


test_message = '''
Traditionally, archaeologists have estimated that the earliest settlers arrived in successive waves in outrigger canoes from South Borneo, possibly throughout the period between 350 BC and 550 AD, while others are cautious about dates earlier than AD 250. In either case, these dates make Madagascar one of the most recent major landmasses on Earth to be settled by humans, predating the settlement of Iceland and New Zealand.[40] It is proposed that Ma'anyan people were brought as laborers and slaves by Javan and Sumatran-Malays in their trading fleets to Madagascar.[41][42][43][44] Dates of settlement of the island earlier than the mid-first millennium AD are not strongly supported.[16] However, there is scattered evidence for much earlier human visits and presence. (See History of Madagascar).[45][46] Archaeological finds such as cut marks on bones found in the northwest and stone tools in the northeast indicate that Madagascar was visited by foragers around 2000 BCE.[47]
      '''
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



test_image_links = [
['https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Atelopus_zeteki1.jpg/330px-Atelopus_zeteki1.jpg','frogGO1'],
['https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Bombina_bombina_1_%28Marek_Szczepanek%29_tight_crop.jpg/330px-Bombina_bombina_1_%28Marek_Szczepanek%29_tight_crop.jpg','froggo'],

]