import googlemaps
import json

import configparser#import the key from secret file
config = configparser.ConfigParser()
config.read("credentials.ini")
#google version getting name
# location = [44.587662,-123.256691]#for testing
def get_name(lat, long):
    gmaps = googlemaps.Client(key=config["DEFAULT"]["key_google"])
    result = gmaps.reverse_geocode((lat, long))
    full_address = result[3]["address_components"][1]["short_name"]
    return full_address
# print(get_name(location[0],location[1]))
