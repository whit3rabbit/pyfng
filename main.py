#!/usr/bin/env python

from bs4 import BeautifulSoup
import mechanize
import argparse
from pprint import pprint
#from random import randint

def select_form(form):
    return form.attrs.get('action', None) == 'index.php'


def get_args():

    # Nameset/Country Dictionary

    name_dict = { 'us':"American",
                  'ar':'Arabic',
                  'au':'Australian',
                  'br':'Brazil',
                  'celat':'Chechen (Latin',
                  'ch': 'Chinese',
                  'zhtw':'Chinese (Traditional)',
                  'hr':'Croatian',
                  'cs':'Czech',
                  'dk':'Danish',
                  'nl':'Dutch',
                  'en':'England/Wales',
                  'er':'Eritrean',
                  'fi':'Finnish',
                  'fr':'French',
                  'gr':'German',
                  'gl':'Greenland',
                  'sp':'Hispanic',
                  'hobbit':'Hobbit',
                  'hu':'Hungarian',
                  'is':'Icelandic',
                  'ig':'Igbo',
                  'it':'Italian',
                  'jpja':'Japanese',
                  'jp':'Japanese (Anglicized)',
                  'tlh':'Klingon',
                  'ninja':'ninja',
                  'no':'Norwegian',
                  'fa':'Persian',
                  'pl':'Polish',
                  'ru':'Russian',
                  'rucyr':'Russian (cyrillic)',
                  'gd':'Scottish',
                  'sl':'Slovenian',
                  'sw':'Swedish',
                  'th':'Thai',
                  'vn':'Vietnamese'
                  }

    country_dict = {'au':'Australia',
                    'as':'Austria',
                    'bg':'Belgium',
                    'br':'Brazil',
                    'ca':'Canada',
                    'cygen':'Cyprus (Anglicized)',
                    'cygk':'Cyprut (Greek)',
                    'cz':'Czech Republic',
                    'dk':'Denmark',
                    'ee':'Estonia',
                    'fi':'Finland',
                    'fr':'France',
                    'gr':'Germany',
                    'gl':'Greenland',
                    'hu':'Hungary',
                    'is':'Iceland',
                    'it':'Italy',
                    'nl':'Netherlands',
                    'nz':'New Zealand',
                    'no':'Norway',
                    'pl':'Poland',
                    'pt':'Portugal',
                    'sl':'Slovenia',
                    'za':'South Africa',
                    'sp':'Spain',
                    'sw':'Sweeden',
                    'sz':'Switzerland',
                    'tn':'Tunisia',
                    'uk':'United Kingdom',
                    'us':'United States',
                    'uy':'Uruguay'
                    }

    # Parser Description
    parser = argparse.ArgumentParser(
        description='Script retrieves data from fakenamegenerator.com')

    # Arguments
    parser.add_argument(
        '-g', '--gender', type=str, help='Gender: random, male, female', required=False, default='male')
    parser.add_argument(
        '-n', '--nameset', type=str, help='Name Set Country', required=False, default='us')
    parser.add_argument(
        '-c', '--country', type=str, help='Country', required=False, default='us')

    # Parse Arguments
    args = parser.parse_args()

    # Set Variables
    gender = args.gender
    nameset = args.nameset
    country = args.country

    # Check for valid name code
    if nameset not in name_dict:
        print('Incorrect Name Set value: {}' % nameset)
        print('Try:')
        for k,v in name_dict:
            print(k,v)
        exit(1)

    # Check for valid name code
    if country not in country_dict:
        print('Incorrect Country Code value: {}' % country)
        print('Try:')
        for k,v in country_dict:
            print(k,v)
        exit(1)

    # Return variables
    return gender, nameset, country


def eat_your_soup(soup):

    # Name
    name = soup.find("div", {"class": "address"}).h3.string

    # Address
    address_find = soup.find("div", {"class": "adr"})
    address_contents = "".join([str(item) for item in address_find.contents])
    address = address_contents.strip().replace('<br/>', '')

    # Mothers Maiden Name
    mothers_maiden = soup.find_all("dl", {"class": "dl-horizontal"})[0].dd.string

    # Social Security Number
    # dd.string doesn't work because there is an advertisement tag
    #social_raw = soup.find_all("dl", {"class": "dl-horizontal"})[1].dd.string
    #print(social_raw)
    #n = 4
    #social_process = social_raw.replace('XXXX', '')
    #four_numbers = ''.join(["%s" % randint(0, 9) for num in range(0, n)])
    #social = social_raw + four_numbers

    # Geo Coordinates
    geos = soup.find_all("dl", {"class": "dl-horizontal"})[2].dd.string

    # Phone
    phone = soup.find_all("dl", {"class": "dl-horizontal"})[3].dd.string

    # Phone CC
    phone_cc = soup.find_all("dl", {"class": "dl-horizontal"})[4].dd.string

    # Birthday
    birthday = soup.find_all("dl", {"class": "dl-horizontal"})[5].dd.string

    # Age
    age = soup.find_all("dl", {"class": "dl-horizontal"})[6].dd.string

    # Zodiac
    zodiac = soup.find_all("dl", {"class": "dl-horizontal"})[7].dd.string

    # Username
    username = soup.find_all("dl", {"class": "dl-horizontal"})[9].dd.string

    # Password
    password = soup.find_all("dl", {"class": "dl-horizontal"})[10].dd.string

    # Website
    website = soup.find_all("dl", {"class": "dl-horizontal"})[11].dd.string

    # Web Browser User Agent
    useragent = soup.find_all("dl", {"class": "dl-horizontal"})[12].dd.string

    # Credit Card
    cc_type = soup.find_all("dl", {"class": "dl-horizontal"})[13].dt.string
    cc_number = soup.find_all("dl", {"class": "dl-horizontal"})[13].dd.string
    cc_expire = soup.find_all("dl", {"class": "dl-horizontal"})[14].dd.string
    cvc2 = soup.find_all("dl", {"class": "dl-horizontal"})[15].dd.string

    # Employer
    employer = soup.find_all("dl", {"class": "dl-horizontal"})[16].dd.string

    # Occupation
    occupation = soup.find_all("dl", {"class": "dl-horizontal"})[17].dd.string

    # Physical
    height = soup.find_all("dl", {"class": "dl-horizontal"})[18].dd.string
    weight = soup.find_all("dl", {"class": "dl-horizontal"})[19].dd.string
    blood_type = soup.find_all("dl", {"class": "dl-horizontal"})[20].dd.string

    # Tracking
    delivery_company = soup.find_all("dl", {"class": "dl-horizontal"})[22].dt.string
    tracking_number = soup.find_all("dl", {"class": "dl-horizontal"})[22].dd.string

    # Make dictionary
    data = {'name': name,
            'address': address,
            'maiden': mothers_maiden,
            'geo': geos,
            'phone': phone,
            'phone_cc': phone_cc,
            'birthday': birthday,
            'age': age,
            'zodiac': zodiac,
            'username': username,
            'password': password,
            'website': website,
            'useragent': useragent,
            'creditcard': {
                'type': cc_type,
                'number': cc_number,
                'expire': cc_expire,
                'cvc2': cvc2
                },
            'employer': employer,
            'occupation': occupation,
            'physical': {
                'height': height,
                'weight': weight,
                'blood type': blood_type
                },
            'tracking': {
                'delivery_company': delivery_company,
                'tracking_number': tracking_number,
                },

            }

    # Return diciontary/results
    return data


def main():

    # Arguments
    gender, nameset, country = get_args()

    # URL
    url = 'http://www.fakenamegenerator.com/'

    # Open URL
    br = mechanize.Browser()
    br.addheaders = \
        [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    # Navitage to website
    br.open(url)

    # Fill forms with values
    br.select_form(predicate=select_form)
    br['gen'] = [gender]
    br['n']   = [nameset]
    br['c']   = [country]

    # Submit form
    br.submit()

    # Get response
    html = br.response().read()
    soup = BeautifulSoup(html, 'lxml')

    data = eat_your_soup(soup)

    pprint(data)

if __name__ == "__main__":
    main()