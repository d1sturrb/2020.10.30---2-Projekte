from requests import get
import json
from pprint import pprint

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/4230588'

weather = get(url).json()["items"]
pprint(weather)

latitude = 47.624219
longitude = 7.669055