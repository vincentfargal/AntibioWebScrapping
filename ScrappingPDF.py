# -------------------------------------------------------------------------------------------------------------------- #
# Antibiotics project
# Test PDF-scrapping
#
# Author: Vincent Fargal
# Date:   21/01/2016
# -------------------------------------------------------------------------------------------------------------------- #

# Import useful libraries - module - functions
import pdfquery
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas
import lxml

# -------------------------------------------------------------------------------------------------------------------- #
# Import list of CIPs to loop over


# -------------------------------------------------------------------------------------------------------------------- #

pdf = pdfquery.PDFQuery("liste_cip7_cip13_1.pdf")

pdf.load()
a = pdf.tree.write("/tmp/yadda", pretty_print=True)

print(a)


# -------------------------------------------------------------------------------------------------------------------- #
