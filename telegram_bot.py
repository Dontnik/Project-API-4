import telegram
import os
from time import sleep

def post_photos_to_telegram(chat_id, path):
    with open(path, 'rb') as photo:

        bot.send_photo(chat_id=chat_id, photo=open(path, 'rb'))



if __name__ == "__main__":
    bot_token = os.getenv('BOT_TOKEN')
    files_in_dirs = os.listdir('images')
    for files_in_dir in files_in_dirs:
        path = os.path.join(files_in_dir)
        file_path = os.path.join(('images'), path)
        delay_seconds = 14400
        sleep(delay_seconds)
