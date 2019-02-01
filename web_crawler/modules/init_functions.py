from .discover import discover
from .crawl import crawl

def add_dictionary():
    name = input('Enter name of new dict:\n')
    path = input('Enter path to the dict you wanna upload:\n')

    try:
        with open(f'./dict/{name}.log', 'w+') as new_file, open(path) as old_file:
            r = old_file.read()
            new_file.write(r)
    except:
        print('Cannot resolve')


def search():

    print('Which searching mode you wanna use?\n')
    print('1 - Crawl\n')
    searching_mode = input('2 - Discover hidden sub-domains\n')

    if searching_mode == '1':
        crawl()
    elif searching_mode == '2':
        discover()
    else:
        print('Invalid data')
