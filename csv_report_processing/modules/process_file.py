from csv import reader
from datetime import datetime
import pycountry
import requests


def process_file(file):

    with open(file) as csv_file:
        file_read = reader(csv_file)

        for row in file_read:
            print(row)


def change_date_format(date_string):
    date = datetime.strptime(date_string, '%m/%d/%Y')
    proper_date = datetime.strftime(date, '%Y-%m-%d')

    return proper_date


def get_country_shortcut(city_name):

    country_code = ''

    for c in list(pycountry.subdivisions):
        if c.name == city_name:
            country_code = c.country_code

    for b in list(pycountry.countries):
        if b.alpha_2 == country_code:
            print(b.alpha_3)



# get_country = input('Input name of the city:\n')
# get_country_shortcut(get_country)

# get_country_shortcut('Encamp')