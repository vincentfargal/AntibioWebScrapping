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
pdf = pdf.load(0)  # first page for trial, pdf.load() if want it all
print(pdf)

text = pdf.pq('LTPage[page_index=0] :in_bbox("100,100,300,300")').text()

# print(text)


# -------------------------------------------------------------------------------------------------------------------- #
