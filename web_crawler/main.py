from pyfiglet import figlet_format
from termcolor import colored

from modules.init_functions import *


header = colored(figlet_format('WEB CRAWLER'), color='magenta')
print(header)
print('\n=================================================================\n')


def main():
    print('What do you want to do?\n')
    print('1 - Upload new dictionary to use, when searching for subdomains (but please remember to stick to the format -> more info in docs)')
    init = input('2 - Crawl/Search for subdomains\n')

    if init == '1':
        add_dictionary()
    elif init == '2':
        search()

main()