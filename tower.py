# Tower of Pysa
# Name inspired by Thomas Nijssen (github @nijssen)
# Python scraper to interface with UC Santa Cruz PISA Class Search

import requests
import json
import re
from bs4 import BeautifulSoup

pisa_url = 'http://localhost/pisa/pisa_raw.txt'

print("Parsing PISA page contents...")

pisa_page = requests.get(pisa_url)

psoup = BeautifulSoup(pisa_page.text, 'html.parser')

name_array = [a.get_text() for a in psoup.findAll('a', attrs={'id' : lambda L: L and L.startswith('class_id_')})]
name_array = [a.replace(u'\xa0', u' ') for a in name_array]
name_array = [a.replace(u'   ', u' ') for a in name_array]

link_array = [a.get('href') for a in psoup.findAll('a', attrs={'href' : lambda L: L and L.startswith('index.php?action=detail')})]

enrollment_array = [a.get_text() for a in psoup.findAll('div', attrs={'class' : 'col-xs-6 col-sm-3'})]
enrollment2_array = [a.get_text() for a in psoup.findAll('div', attrs={'class' : 'col-xs-6 col-sm-6'})]

json_name_obj = json.dumps(name_array)
json_link_obj = json.dumps(link_array)
json_enrollment_obj = json.dumps(enrollment_array)
json_enrollment2_obj = json.dumps(enrollment2_array)

json_output = open("/var/www/html/pisa/names.json", "w")
json_output.write(json_name_obj)
json_output.close()

json_output = open("/var/www/html/pisa/links.json", "w")
json_output.write(json_link_obj)
json_output.close()

json_output = open("/var/www/html/pisa/meta.json", "w")
json_output.write(json_enrollment_obj)
json_output.close()

json_output = open("/var/www/html/pisa/meta2.json", "w")
json_output.write(json_enrollment2_obj)
json_output.close()

print("Wrote JSON with " + str(len(name_array)) + " courses.")
