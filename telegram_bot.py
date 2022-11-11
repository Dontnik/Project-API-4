import telegram


bot = telegram.Bot(token='5762502045:AAF_0v5JWQUSw1CzTmdGDGN3KW0zkj2z8aY')
print(bot.get_me())
{"first_name": "Toledo's Palace Bot", "username": "ToledosPalaceBot"}
bot.send_message(text='Hi everyone!', chat_id='@space_download')
bot.send_document(chat_id='@space_download', document=open('images/22nasa_apod.gif', 'rb'))