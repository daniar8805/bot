import requests
import json
url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"almaty"}

headers = {
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
    'x-rapidapi-key': "908954c233mshb53648f71f35a8dp162f14jsndee2134ed326"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)


temp=json.loads(response.text)

temperature=temp['current']
print(temperature)