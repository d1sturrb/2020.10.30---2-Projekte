from requests import get
import json
from pprint import pprint

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'

stations = get(url).json()['items']

pprint(stations)

"""
{'weather_stn_id': 4230588,
  'weather_stn_lat': 45.680486,
  'weather_stn_long': -111.052448,
  'weather_stn_name': 'Yoda'},
  """