from pyfiglet import figlet_format
from termcolor import colored

header = colored(figlet_format('WEB CRAWLER'), color='magenta')
print(header)
print('\n=================================================================\n')
print('Which searching mode you wanna use?\n')
print('Use one of the following:\n')
print('1 - Crawl\n')
searching_mode = input('2 - Discover hidden sub-domains\n')

print(searching_mode)