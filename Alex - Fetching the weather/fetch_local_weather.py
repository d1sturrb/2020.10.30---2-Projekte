from requests import get
import json
from pprint import pprint
from haversine import haversine

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

#latitude, longitude
home = [47.624219, 7.669055]
#my_latitude = 47.624219
#my_longitude = 7.669055

all_stations = get(stations).json()["items"]

def find_closest(chosen_longitude, chosen_latitude):
    smallest = 20036
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        distance = haversine(chosen_longitude, chosen_latitude, station_lon, station_lat)
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
    return closest_station

closest_station_id = find_closest(home[0], home[1])

weather += str(closest_station_id)

my_weather = get(weather).json()["items"]
pprint(my_weather)