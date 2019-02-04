from csv import reader, writer
from datetime import datetime
import pycountry
import requests
from termcolor import colored
import os

from .process_engine import *



def process_file(file, new_name):
    """This function will init processing given .csv file"""

    with open(file) as csv_file, open(f'{os.getcwd()}/{new_name}.csv', 'w+') as new_file:

        if not file[-3:] == 'csv':                      # Check if passed file is .csv
            return print(colored('You have to pass .csv file!', color='red'))

        file_read = reader(csv_file)

        if not csv_file.read(1):                               # Check if passed file contain data
            return print(colored('No data in the file!', color='red'))

        for row in file_read:
            date = change_date_format(row[0])           # Change data as specified in task
            code = get_country_shortcut(row[1])
            impressions = int(row[2])

            new_file_write = writer(new_file)
            new_file_write.writerow([date, code, impressions, row[3]])



