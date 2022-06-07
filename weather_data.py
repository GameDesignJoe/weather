import urllib.parse
import os
import requests
from pprint import pprint

# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}

endpoint = 'http://api.openweathermap.org/'


def find_lat_long_of_city(city_name, country_code='AU'):
    city_name = urllib.parse.quote(city_name)
    print(city_name)
    path = 'geo/1.0/direct'
    query_parameters = f'?q={city_name},{country_code}&appid={os.environ["OPENWEATHER_API_KEY"]}'
    request = f'{endpoint}{path}{query_parameters}'
    # print(request)
    response = requests.get(request)
    cities = response.json()
    pprint(cities)
    location = {}
    if len(cities) > 0:
        location = {'lat': cities[0].get('lat'), 'lon': cities[0].get('lon')}
    return location