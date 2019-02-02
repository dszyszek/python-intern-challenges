import datetime
import requests

from .make_report import make_report

def discover():
    print('\n=================================================================')
    print('Discover mode')
    print('=================================================================\n')

    page = input('Enter name of the page:\n')
    dic = input('\nEnter name of your searching-dictionary (if you don\'t have one, you can use one of the predefined dicts: pre-min or pre-max)\n')

    find(page, dic)


def find(url, log_file):
    found = []

    with open(f'./dict/{log_file}.log', 'r') as file:

        for line in file:
            single_line = line.strip()
            print(f'Testing: {single_line}.{url}')

            try:
                req = requests.get(f'http://{single_line}.{url}', timeout=2)
                if req:
                    found.append(f'{single_line}.{url}')
                    # print(f'Found sub-domain! {single_line}.{url}')

            except requests.exceptions.ConnectionError:
                pass

        if len(found) == 0:
            print('No results')
        else:
            make_report(f'http://{url}', found, 'subdomains', 'discover')




