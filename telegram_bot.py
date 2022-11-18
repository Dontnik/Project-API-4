import telegram
import os
from time import sleep

def post_photos_to_telegram(chat_id, path):

    bot.send_photo(chat_id='@space_download', photo=open(path, 'rb'))


if __name__ == "__main__":
    bot = telegram.Bot(token='5762502045:AAF_0v5JWQUSw1CzTmdGDGN3KW0zkj2z8aY')
    files_in_dirs = os.listdir('images')
    for files_in_dir in files_in_dirs:
        path = os.path.join(files_in_dir)
        file = os.path.join(str('images'), path)
        post_photos_to_telegram('@space_download', file)
        sleep(14400)