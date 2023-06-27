import time
from typing import Generator

from bs4 import BeautifulSoup
import requests


def links_parser(url: str) -> Generator:
    HTTP = 'http://'
    FORMAT = '.jpg'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    frogs_imgs = soup.findAll('script')
    links = str(frogs_imgs).split('\n')
    for link in links:
        if HTTP in link and FORMAT in link:
            yield link.replace('\r', '').replace('"', '').replace(',', '').strip()



