import requests

url = "https://weatherapi-com.p.rapidapi.com/astronomy.json"

querystring = {"q":"London"}

headers = {
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
    'x-rapidapi-key': "908954c233mshb53648f71f35a8dp162f14jsndee2134ed326"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)