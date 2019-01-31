import requests



def discover():
    print('\n=================================================================\n')
    print('Discover mode')
    print('\n=================================================================\n')

    page = input('Enter url address:\n')

    find(page)




def find(url):
    a = requests.get(url)
    print(a.text)
