from pyfiglet import figlet_format
from termcolor import colored
import os.path

from modules.process_file import process_file

header = colored(figlet_format('CSV REPORT PROCESSING'), color='cyan')
print(header)
print('\n=================================================================\n')


def init():
    file = input('Enter path to .csv file you wanna reorganize:\n')
    new_file_name = input('Enter name of new .csv file:\n')

    if os.path.isfile(f'./processed_files/{new_file_name}'):     # Change name of file to prevent overwriting
        new_file_name = f'{new_file_name}-copy'
        print(f'File with such name exist! Name of your file is changed to {new_file_name}')

    process_file(file, new_file_name)


init()
