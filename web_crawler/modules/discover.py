import requests



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
            try:
                single_line = line.strip()
                req = requests.get(f'http://{single_line}.{url}')

                if req:
                    found.append(req)
                    print(f'Found sub-domain! {single_line}.{url}')

            except requests.exceptions.ConnectionError:
                pass
        if len(found) == 0:
            print('No results')

