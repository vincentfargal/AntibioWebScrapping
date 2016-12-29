# Test web-scrapping

import urllib.request

response = urllib.request.urlopen('http://www.codage.ext.cnamts.fr/codif/bdm_it//fiche/index_fic_medisoc.php?p_code_cip=3400933047467&p_site=AMELI')
page_source = response.read()
print(page_source)

