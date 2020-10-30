from math import radians, cos, sin, asin, sqrt

# convert degrees to radians
def convert_degrees_to_radians(arg_degree):
    arg_radian = radians(arg_degree)
    return arg_radian

def haversine(lon1, lat1, lon2, lat2):
    lon1 = convert_degrees_to_radians(lon1)
    lat1 = convert_degrees_to_radians(lat1)
    lon2 = convert_degrees_to_radians(lon2)
    lat2 = convert_degrees_to_radians(lat2)
    
    delta_lon = lon2 - lon1
    delta_lat = lat2 - lat1
    
    a = sin(delta_lat/2)**2 + cos(lat1) * cos(lat2) * sin(delta_lon/2)**2
    distance = 2 * asin(sqrt(a)) * 6371 # 6371 is the radius of the Earth
    return distance