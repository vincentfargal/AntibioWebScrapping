# Test web-scrapping
# Vincent Fargal
# Projet Antibio


import urllib.request



# I - URL fetching

# Load content of URL
URL = 'http://www.codage.ext.cnamts.fr/codif/bdm_it//fiche/index_fic_medisoc.php?p_code_cip=3400933047467&p_site=AMELI'
response = urllib.request.urlopen(URL)
page_source = response.read()
page_source = str(page_source)
print(page_source)

# Save it to txt file
if __name__ == '__main__':
    with open("URL.txt", "w") as a:
        a.write(page_source)

# Will need to create a database of all CIP to look for and to loop through them in order to get the URL of each
# research in a txt file



# II - Collect data in URL txt files

