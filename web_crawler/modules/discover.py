import requests



def discover():
    print('\n=================================================================')
    print('Discover mode')
    print('=================================================================\n')

    page = input('Enter name of the page:\n')
    dic = input('\nEnter name of your searching-dictionary (if you don\'t have one, just type pre)\n')

    find(page, dic)




def find(url, log_file):

    with open(f'./dict/{log_file}.log', 'r') as file:
        try:
            for line in file:
                single_line = line.strip()
                req = requests.get(f'http://{single_line}.{url}')

                if req:
                    print(f'Found sub-domain! www.{single_line}.{url}')
        except requests.exceptions.ConnectionError:
            pass

