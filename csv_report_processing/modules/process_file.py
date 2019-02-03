from csv import reader, writer
from datetime import datetime
import pycountry
import requests


def process_file(file, new_name):
    """This function will init processing given .csv file"""

    with open(file) as csv_file, open(f'./processed_files/{new_name}.csv', 'w+') as new_file:
        file_read = reader(csv_file)

        for row in file_read:
            date = change_date_format(row[0])
            code = get_country_shortcut(row[1])
            impressions = int(row[2])

            new_file_write = writer(new_file)
            new_file_write.writerow([date, code, impressions, row[3]])


def change_date_format(date_string):
    """This function will change form of given date into required in task"""

    date = datetime.strptime(date_string, '%m/%d/%Y')       # Change date string into datetime object
    proper_date = datetime.strftime(date, '%Y-%m-%d')       # Change date formatting into required one

    return proper_date


def get_country_shortcut(city_name):
    """This function will try to find three-letter country code of country, in which given city is located"""

    country_code = ''

    try:
        for c in list(pycountry.subdivisions):      # Extract two-letter country code from name of city
            if c.name == city_name:
                country_code = c.country_code

        if not country_code:
            raise ValueError()

        for b in list(pycountry.countries):         # change extracted two-letter country code to three-letter one
            if b.alpha_2 == country_code:
                return b.alpha_3
    except:
        return 'XXX'
