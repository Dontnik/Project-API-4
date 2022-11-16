import telegram

def auto_post_photos_to_telegram(chat_id, path):

    bot.send_photo(chat_id='@space_download', photo=open('images/2nasa_apod.gif', 'rb'))


if __name__ == "__main__":

    bot = telegram.Bot(token='5762502045:AAF_0v5JWQUSw1CzTmdGDGN3KW0zkj2z8aY')
    print(bot.get_me())
    {"first_name": "Toledo's Palace Bot", "username": "ToledosPalaceBot"}
    bot.send_message(text='Hi everyone!', chat_id='@space_download')
    auto_post_photos_to_telegram('@space_download', 'images/2nasa_apod.gif')