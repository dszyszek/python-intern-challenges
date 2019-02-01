import re


def crawl():
    print('\n=================================================================')
    print('Crawl mode')
    print('=================================================================\n')

    page = input('Enter name of the page:\n')

    site_map(page)

def site_map(url):
    print(url)