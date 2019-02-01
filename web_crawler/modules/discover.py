import datetime
import requests

from .make_report import make_report

def discover():
    print('\n=================================================================')
    print('Discover mode')
    print('=================================================================\n')

    page = input('Enter name of the page:\n')
    dic = input('\nEnter name of your searching-dictionary (if you don\'t have one, just type pre)\n')

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
            report_decision = input('Do you want to make report? (y/n)\n')

            if report_decision == 'y':
                make_report(url, found, 'subdomains')
            elif report_decision == 'n':
                pass
            else:
                print('Unknown command')



