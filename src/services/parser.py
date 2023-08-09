import asyncio
from random import randint
from typing import AsyncGenerator
import httpx
from bs4 import BeautifulSoup
from src.settings import Settings

settings = Settings()


async def _image_parser(url: str) -> list[str]:
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


async def image_generator() -> AsyncGenerator:
    images = await _image_parser(settings.url_site)
    yield images[randint(0, len(images) - 1)]


async def random_number() -> int:
    MIN_NUM = 0
    MAX_NUM = 100
    return randint(MIN_NUM, MAX_NUM)


async def main():
    gen = image_generator()
    awaitable = anext(gen)
    result = await awaitable
    print(result)


if __name__ == '__main__':
    # asyncio.run(main())
    pass
