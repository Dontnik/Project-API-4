import requests
from urllib.parse import urlparse
import os

def download_image(filename, folder, url, params=None):
    os.makedirs(folder, exist_ok=True)
    response = requests.get(url, params=params)
    response.raise_for_status()
    path = os.path.join(("images")path)

    with open(path, 'wb') as file:
        file.write(response.content)


def get_extension(url):
    parsed_url = urlparse(url)
    link_parts = os.path.splitext(parsed_url.path)
    return link_parts[1]

