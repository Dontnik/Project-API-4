import requests
import os
import datetime
from tools import download_image
from tools import get_extension

def fetch_nasa_apod(api_key, folder = 'images'):
    url = 'https://api.nasa.gov/planetary/apod'
    count = 30
    response = requests.get(url, params={'api_key': api_key, 'count': count})
    response.raise_for_status()
    for number, photo in enumerate(response.json()):
        if photo['media_type'] == 'image':
            link = photo['url']
            image_name = f'{number}nasa_apod{get_extension(link)}'
            download_image(image_name, folder, link)

def fetch_nasa_epic(api_key, folder = 'images'):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params = {'api_key': api_key})
    response.raise_for_status()
    for number, photo in enumerate(response.json()):
        pic_name = photo['image']
        date = datetime.datetime.fromisoformat(photo['date'])
        formated_date = datetime.datetime.strftime(date, '%Y/%m/%d')
        pic_url = f'https://api.nasa.gov/EPIC/archive/natural/{formated_date}/png/{pic_name}.png'
        download_image(f'{pic_name}.png', folder, pic_url, params={'api_key': api_key})

if __name__ == "__main__":
    api_key = os.getenv('API_KEY')
    fetch_nasa_apod(api_key, folder='images')
    fetch_nasa_epic(api_key, folder='images')