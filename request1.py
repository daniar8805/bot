import requests

import json


url = "https://wordsapiv1.p.rapidapi.com/words/incredible/definitions"

headers = {
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': "908954c233mshb53648f71f35a8dp162f14jsndee2134ed326"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

data = json.loads(response.text)

# print(data['definitions'])

for el in data['definitions']:
	print(el['definition'])