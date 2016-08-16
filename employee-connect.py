import requests
import sys
import re
import json

search = sys.argv[1]
data = requests.get('http://employee-directory.www.pdrop.net/directory.json')
parsed_string = ""
database={}

for person in data.json():
    key = person['first']
    database.setdefault(key, [])
    database[key].append(str(person))

for i in database[search]:
    string = re.sub("u\'+", "" ,i)
    string = re.sub("'", "", string)
    string = re.sub(",", "\n", string)
    string = re.sub("{", "", string)
    string = re.sub("}", "", string)
    print string + "\n"



