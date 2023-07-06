from random import randint
from typing import AsyncGenerator
import httpx
from bs4 import BeautifulSoup
from src.settings import Settings

settings = Settings()


async def image_parser(url: str) -> list[str]:
    HTTP = 'http://'
    FORMAT = '.jpg'
    formated_image = []
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    images = str(soup.findAll('script')).split('\n')
    for image in images:
        if HTTP in image and FORMAT in image:
            formated_image.append(image.replace('\r', '').replace('"', '').replace(',', '').strip())
    return formated_image


async def image_gen(images: list[str]) -> AsyncGenerator:
    yield images[randint(0, len(images) - 1)]


if __name__ == '__main__':
    pass
