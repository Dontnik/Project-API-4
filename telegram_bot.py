import os
from time import sleep
import telegram
import random
from dotenv import load_dotenv, find_dotenv



def post_photos_to_telegram(chat_id, path, bot):
    with open(path, 'rb') as photo:
        bot.send_message(text='Photo of the day', chat_id=chat_id)
        bot.send_photo(chat_id=chat_id, photo=photo)



if __name__ == "__main__":
    load_dotenv(find_dotenv())
    chat_id = os.getenv('TG_CHAT_ID')
    bot_token = os.getenv('TG_BOT_TOKEN')
    bot = telegram.Bot(token=bot_token)
    files_in_dirs = os.listdir('images')
    while True:
        path = random.choice(files_in_dirs)
        file_path = os.path.join(('images'), path)
        post_photos_to_telegram(chat_id, file_path, bot)
        delay_seconds = 36000
        sleep(delay_seconds)
