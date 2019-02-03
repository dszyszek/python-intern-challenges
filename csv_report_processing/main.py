from pyfiglet import figlet_format
from termcolor import colored

from modules.process_file import process_file

header = colored(figlet_format('CSV REPORT PROCESSING'), color='cyan')
print(header)
print('\n=================================================================\n')


def init():
    file = input('Enter path to .csv file you wanna reorganize:\n')
    process_file(file)


init()
