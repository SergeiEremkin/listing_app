from bs4 import BeautifulSoup
import requests


def parse_frogs(url: str) -> list[str]:
    HTTP = 'http://'
    FORMAT = '.jpg'
    all_links = []
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    # print(soup.prettify())
    frogs_imgs = soup.findAll('script')
    links = str(frogs_imgs).split('\n')
    for link in links:
        if HTTP in link and FORMAT in link:
            all_links.append(link.replace('\r', '').replace('"', '').replace(',', '').strip())
    return all_links


if __name__ == '__main__':
    print(parse_frogs('http://allaboutfrogs.org/funstuff/randomfrog.html'))
