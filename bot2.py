import telebot

import json

import requests
bot2=telebot.TeleBot('1965526434:AAH6exE3VNpplrgoyITbtalgh88bJfUWLKo')


@bot2.message_handler(commands=['start'])
def start(message):
	bot2.send_message(message.chat.id, f'hello!{message.from_user.first_name}')



# @bot2.message_handler(content_types=['text'])
# def definition(message):
# 	url = f"https://wordsapiv1.p.rapidapi.com/words/{message.text}/definitions"

# 	headers = {
#     'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
#     'x-rapidapi-key': "908954c233mshb53648f71f35a8dp162f14jsndee2134ed326"
#     }

# 	response = requests.request("GET", url, headers=headers)

# 	print(response.text)

# 	data = json.loads(response.text)

# 	# print(data['definitions'])

# 	for el in data['definitions']:
# 		bot2.send_message(message.chat.id, el['definition'])


@bot2.message_handler(countent_types=['text'])
def weather(message):
	url = "https://weatherapi-com.p.rapidapi.com/current.json"

	querystring =  {f"q":{message.text}}

	headers = {
	    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
	    'x-rapidapi-key': "908954c233mshb53648f71f35a8dp162f14jsndee2134ed326"
	    }

	response = requests.request("GET", url, headers=headers, params=querystring)

	# print(response.text)


	temp=json.loads(response.text)

	temperature=temp['current']
	bot2.send_message(message.chat.id,temperature)

bot2.polling(non_stop=True)
