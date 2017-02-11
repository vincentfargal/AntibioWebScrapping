# -------------------------------------------------------------------------------------------------------------------- #
# Antibiotics project
# Test web-scrapping - Beautiful Soup
#
# Author: Vincent Fargal
# Date:   15/01/2016
# -------------------------------------------------------------------------------------------------------------------- #

# Import useful libraries - module - functions
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas

# -------------------------------------------------------------------------------------------------------------------- #
# Import list of CIPs to loop over


# -------------------------------------------------------------------------------------------------------------------- #

URL = 'http://www.codage.ext.cnamts.fr/codif/bdm_it//fiche/index_fic_medisoc.php?p_code_cip=3400933047467&p_site=AMELI'

sauce = urllib.request.urlopen(URL).read()   # Source code
soup = BeautifulSoup(sauce, "lxml")   # Source like in the browser
# print(soup)

# -------------------------------------------------------------------------------------------------------------------- #

# Get tables text (including titles in div tags)
tables = soup.find_all('table')  # finds all tables in our url
# print(table)
mylist = []
CIP = []
PrixFab = []
PrixPublic = []
TauxRemb = []
DateAppli = []
DateOpposPTTC = []
DateJO = []


for table in tables:
    out = table.get_text()
    mylist.append(out)
    #print(out)  # .get_text() strips all tags and returns a string containing the text only.

# Object containing all the data we want
raw_tables = mylist[5]
# print(raw_tables)


# Retrieve CIP
s = re.search("CIP:(.*)", raw_tables)
CIP.append(s.group(1))
# print(CIP)

HRemb = raw_tables[raw_tables.find("Date JO")+9:raw_tables.find("\n\n\n\n\n\nHistorique pour les collectivités")]
# print(HRemb)

rows = HRemb.split('\n')  # split the string into a list of the line
print(rows)


# Replace dashes by a NA (XX) value of the correct length
for i, item in enumerate(rows):
    if item[0] == "-":
        rows[i] = 'X.XXX €' + rows[i][1:]

for i, item in enumerate(rows):
    if item[7] == "-":
        rows[i] = rows[i][:7] + 'X.XX €' + rows[i][8:]

for i, item in enumerate(rows):
    if item[13] == "-":
        rows[i] = rows[i][:13] + 'XX %' + rows[i][14:]

for i, item in enumerate(rows):
    if item[17] == "-":
        rows[i] = rows[i][:17] + 'XX/XX/XXXX' + rows[i][18:]

for i, item in enumerate(rows):
    if item[27] == "-":
        rows[i] = rows[i][:27] + 'XX/XX/XXXX' + rows[i][28:]

for i, item in enumerate(rows):
    if item[37] == "-":
        rows[i] = rows[i][:37] + 'XX/XX/XXXX' + rows[i][38:]
print(rows)


# Store data in the correct lists
for row in rows:
    PrixFab.append(row[:5])
    PrixPublic.append(row[7:11])
    TauxRemb.append(row[13:15])
    DateAppli.append(row[17:27])
    DateOpposPTTC.append(row[27:37])
    DateJO.append(row[37:47])

n = len(rows)

# Data frame
output = pandas.DataFrame({'CIP':CIP*n,
                           'PrixFab':PrixFab,
                           'PrixPublic': PrixPublic,
                           'TauxRemb': TauxRemb,
                           'DateAppli': DateAppli,
                           'DateOpposPTTC': DateOpposPTTC,
                           'DateJO': DateJO})

print(output)
output.to_csv('output.csv')


# -------------------------------------------------------------------------------------------------------------------- #

# print(soup.title.string)  # Title of the web-page

# print(soup.p)  # Find first tag p
# print(soup.find_all('p'))  # Find all p tags

# print(soup.get_text())

# Get paragraphs (without the tags) marked-up with p tag
# for paragraph in soup.find_all('p'):
#     print(paragraph.text)


# Get urls (without the tags) marked-up with a tag
# for url in soup.find_all('a'):
#     print(url.get('href))

# nav tags for navigation bars on websites and links on which user can click

# Finds all text in body in p tags
# body = soup.body
# for paragraph in body.find_all('p'):
#     print(paragraph.text)

# Get tables titles - 2 DIV tags at beginning of each table
# divs = soup.find_all('div', {'class':'titrePage'})  # get the div tags that are of titlePage class
# for div in divs:
#     print(div.get_text())


# Tables in HTML
# TH table header
# TR table row
# TD table data


# ----------------------------------- #
# table = soup.table
# print(table)
# table = soup.find('table')
# print(table)
# table_rows = table.find_all('tr')  # in the tables, get the table rows
#
# for tr in table_rows:
#     td = tr.find_all('td')  # in the table rows get the table data
#     row = [i.text for i in td]
#     print(row)
# ----------------------------------- #


# Using pandas

# dfs = pandas.read_html(URL, header=0)
# for df in dfs:
#     print(df)
#     df.to_csv('output.csv', sep=',')


