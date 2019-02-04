from csv import reader, writer
from datetime import datetime
import pycountry
from termcolor import colored
import os
import sys

from .process_engine import *



def process_file(file, new_name):
    """This function will init processing given .csv file"""

    with open(file) as csv_file, open(f'{os.path.split(os.path.abspath(__file__))[0]}/../processed_files/{new_name}.csv', 'w+') as new_file:

        if not file[-3:] == 'csv':                      # Check if passed file is .csv
            print(colored('You have to pass .csv file!', color='red'))

            return 0

        file_read = reader(csv_file)

        if not csv_file.read(1):                               # Check if passed file contain data
            os.remove(f'{os.getcwd()}/../processed_files/{new_name}.csv')   # Remove created empty file
            print(colored('No data in the file!', color='red'))

            return 0

        new_file_write = writer(new_file)
        new_file_write.writerow(['Date', 'Country_code', 'Number of impressions', 'CTR'])

        for row in file_read:
            date = change_date_format(row[0])           # Change data as specified in task
            code = get_country_shortcut(row[1])
            impressions = int(row[2])

            new_file_write.writerow([date, code, impressions, row[3]])



