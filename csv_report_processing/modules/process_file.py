from csv import reader
from datetime import datetime
import pycountry
import requests


def process_file(file):
    '''This function will init processing given .csv file'''
    with open(file) as csv_file:
        file_read = reader(csv_file)

        for row in file_read:
            print(row)


def change_date_format(date_string):
    '''This function will change form of given date into required in task'''
    date = datetime.strptime(date_string, '%m/%d/%Y')       # Change date string into datetime object
    proper_date = datetime.strftime(date, '%Y-%m-%d')       # Change date formatting into required one

    return proper_date


def get_country_shortcut(city_name):
    '''This function will try to find three-letter country code of country, in which given city is located'''
    country_code = 'XXX'

    try:
        for c in list(pycountry.subdivisions):      # Extract two-letter country code from name of city
            if c.name == city_name:
                country_code = c.country_code

        for b in list(pycountry.countries):         # change extracted two-letter country code to three-letter one
            if b.alpha_2 == country_code:
                return b.alpha_3
    except:
        return country_code



# get_country = input('Input name of the city:\n')
# res = get_country_shortcut(get_country)
# print(res)

# get_country_shortcut('Encamp')