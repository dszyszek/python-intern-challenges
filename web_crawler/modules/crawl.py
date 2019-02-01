import re
from urllib.parse import urljoin
import requests

target = []


def crawl():
    print('\n=================================================================')
    print('Crawl mode')
    print('=================================================================\n')

    page = input('Enter name of the page:\n')

    if not 'http://' or not 'https://' in page:
        page = f'http://{page}'

    site_map(page)


def get_links(url):
    res = requests.get(url)
    return re.findall('(?:href=")(.*?)"', res.text)


def site_map(url):
    links = get_links(url)

    # print(links)

    for link in links:
        link = urljoin(url, link)

        if url in link and link not in target:
            target.append(link)
            print(link)
            site_map(link)
