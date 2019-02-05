from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from pprint import pprint

from .make_report import make_report


links_global = set()
result_dict = {}
url_first = ''


def crawl():
    global url_first

    print('\n=================================================================')
    print('Crawl mode')
    print('=================================================================\n')

    page = input('Enter name of the page:\n')

    if not ('http://' or 'https://') in page:
        page = f'http://{page}'

    url_first = page

    site_map(page)
    print('\nResults:\n')
    pprint(result_dict)                                # Print results from crawling

    make_report(url_first, result_dict, 'maps_of_sites', 'crawl')


def site_map(url):
    global url_first
    res = requests.get(url)
    links_current = set()
    links_no_follow = set()

    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.find('title')

    if title:
        title = title.get_text()
    else:
        title = 'No title'

    links = soup.find_all('a', href=True)

    for link in links:
        link = urljoin(url, link['href'])

        if url_first in link and link not in links_global:
            print(f'Testing: {link}')
            links_global.add(link)
            links_current.add(link)

        elif url_first in link and  link in links_global and link not in links_current:
            links_no_follow.add(link)

    if url not in result_dict:
        result_dict[url] =  {
            'title': title,
            'links': links_current.union(links_no_follow)
        }

    for x in links_current:
        if not x[-3:] == 'pdf':
            site_map(x)


