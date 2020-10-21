import googlemaps
import json
import time
start_time = time.time()

import configparser#import the key from secret file
config = configparser.ConfigParser()
config.read("credentials.ini")#stored keys outside respository.
#google version getting name. Uses googlemaps module. and the key is kept secret
# location = [44.630474,-123.273361]#for testing

def get_name_google(lat, long):

    gmaps = googlemaps.Client(key=config["DEFAULT"]["key_google"])#personal API key
    result = gmaps.reverse_geocode((lat, long))#gets json

    #check for the right name in the json file
    abrev = ["Rd", "Ln", "St", "Ave", "Dr", "Way", "Pl", "Blvd", "Ct", "Terrace", "I-", "Hwy", "Cir", "Aly", "Bldg","Expy", "Fwy", "Gtwy", "Pl", "Ste", "Vw", "Sta"]

    full_address = ""
    #checks for street names and filter names from cities, counties, etc.If it gets as result a name that is not in the abrev list, will dismiss it and search again.
    for i in range(0,5):
        try:
            if any(x in result[i]["address_components"][1]["short_name"] for x in abrev):
                full_address = result[i]["address_components"][1]["short_name"]
        except:
            full_address = result[1]["address_components"][1]["short_name"]

    return full_address

# print(get_name_google(location[0],location[1]))
# print("--- %s seconds ---" % (time.time() - start_time))
