import googlemaps
import json

#google version getting name

location = [44.660458,-123.280029]

def get_name(lat, long):
    gmaps = googlemaps.Client(key='AIzaSyB1ym7awZxyyWrmI5Y7OTAQDEyasZZMG0o')
    result = gmaps.reverse_geocode((lat, long))
    full_address = result[3]["address_components"][1]["short_name"]
    # signal = 0
    # text =  full_address.split(",")
    # resultado = text[0].split(" ")
    return full_address
    # return ' '.join(resultado[1:])

print(get_name(location[0],location[1]))

















# import requests
#
# def get_name(lat, long):
#     origen = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(lat) + "," + str(long) + "&key=AIzaSyB1ym7awZxyyWrmI5Y7OTAQDEyasZZMG0o"
#
#     response = requests.get(origen).json()
#     print(response["results"][0]["address_components"][1]['short_name'])
#
# get_name(44.587662,-123.256691)
