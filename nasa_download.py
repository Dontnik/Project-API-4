import requests
import datetime
from tools import download_image
from tools import get_extension

api_key = 'm9HmwKyIzN2Uihp5bkoZj8XD8F9M9090L2G3S4r5'
def fetch_nasa_apod(api_key, folder = 'images'):
    api_key = 'm9HmwKyIzN2Uihp5bkoZj8XD8F9M9090L2G3S4r5'
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params={'api_key': api_key, 'count': 30})
    response.raise_for_status()
    for number, photo in enumerate(response.json()):
        if photo['media_type'] == 'image':
            link = photo['url']
            image_name = f'{number}nasa_apod{get_extension(link)}'
            download_image(image_name, folder, link)

def fetch_nasa_epic(api_key, folder = 'images'):
    api_key = 'm9HmwKyIzN2Uihp5bkoZj8XD8F9M9090L2G3S4r5'
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params = {'api_key': api_key})
    response.raise_for_status()
    for number, photo in enumerate(response.json()):
        pic_name = photo['image']
        datetime_date = datetime.datetime.fromisoformat(photo['date'])
        formated_date = datetime.datetime.strftime(datetime_date, '%Y/%m/%d')
        pic_url = f'https://api.nasa.gov/EPIC/archive/natural/{formated_date}/png/{pic_name}.png'
        download_image(f'{pic_name}.png', folder, pic_url, params={'api_key': api_key})

if __name__ == "__main__":

    fetch_nasa_apod(api_key, folder='images')
    fetch_nasa_epic(api_key, folder='images')