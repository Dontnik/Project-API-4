import requests
from tools import download_image

def fetch_spacex_last_launch(folder = 'images', id = '5eb87d47ffd86e000604b38a'):
    url = f'https://api.spacexdata.com/v5/launches/{id}'
    response = requests.get(url)
    links = response.json()['links']['flickr']['original']
    for number, link in enumerate(links):
        filename = f'spacex_{number}.jpg'
        download_image(filename, folder, link)

if __name__ == "__main__":

    fetch_spacex_last_launch(folder='images', id='5eb87d47ffd86e000604b38a')
