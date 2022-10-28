import requests
from urllib.parse import urlparse
import os
import datetime


def download_image(filename, folder, url, params=None):
    os.makedirs(folder, exist_ok=True)
    response = requests.get(url, params=params)
    response.raise_for_status()
    path = f'{folder}/{filename}'

    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_nasa_apod(api_key, folder = 'images'):
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params={'api_key': api_key, 'count': 30})
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
        datetime_date = datetime.datetime.fromisoformat(photo['date'])
        formated_date = datetime.datetime.strftime(datetime_date, '%Y/%m/%d')
        pic_url = f'https://api.nasa.gov/EPIC/archive/natural/{formated_date}/png/{pic_name}.png'
        download_image(f'{pic_name}.png', folder, pic_url, params={'api_key': api_key})

def get_extension(url):
    parsed_url = urlparse(url)
    link_parts = os.path.splitext(parsed_url.path)
    return link_parts[1]
def fetch_spacex_last_launch(folder = 'images', id = '5eb87d47ffd86e000604b38a'):
    url = f'https://api.spacexdata.com/v5/launches/{id}'
    response = requests.get(url)
    links = response.json()['links']['flickr']['original']
    for number, link in enumerate(links):
        filename = f'spacex_{number}.jpg'
        download_image(filename, folder, link)

api_key = 'm9HmwKyIzN2Uihp5bkoZj8XD8F9M9090L2G3S4r5'
fetch_spacex_last_launch(folder='images', id='5eb87d47ffd86e000604b38a')
fetch_nasa_apod(api_key, folder='images')
fetch_nasa_epic(api_key, folder='images')