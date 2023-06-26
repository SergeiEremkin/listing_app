import time
from typing import Generator

from bs4 import BeautifulSoup
import requests


def _links_parser(url: str) -> Generator:
    HTTP = 'http://'
    FORMAT = '.jpg'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    frogs_imgs = soup.findAll('script')
    links = str(frogs_imgs).split('\n')
    for link in links:
        if HTTP in link and FORMAT in link:
            yield link.replace('\r', '').replace('"', '').replace(',', '').strip()


def cron(timer: int, links: Generator = _links_parser('http://allaboutfrogs.org/funstuff/randomfrog.html')):
    # 24 часа = 60 сек * 60 * 24 = 86400
    while True:
        print(next(links))
        time.sleep(timer)


if __name__ == '__main__':
    cron(5)
