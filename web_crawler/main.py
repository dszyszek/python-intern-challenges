from pyfiglet import figlet_format
from termcolor import colored

from modules.discover import discover

header = colored(figlet_format('WEB CRAWLER'), color='magenta')
print(header)
print('\n=================================================================\n')
print('Which searching mode you wanna use?\n')
print('Use one of the following:\n')
print('1 - Crawl\n')
searching_mode = input('2 - Discover hidden sub-domains\n')

if searching_mode == '1':
    pass
elif searching_mode == '2':
    discover()
else:
    print('Invalid data')
