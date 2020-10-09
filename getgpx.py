import gpxpy
# from directions import get_name
from google import get_name

file = open('09_27_20.gpx', 'r')
list = gpxpy.parse(file)

class puntos:
    def __init__(self,lat, long, elev, time):
        self.__lat = lat
        self.__long = long
        self.__elev = elev
        self.__time = time

    def get_lat(self):
        return self.__lat

    def get_long(self):
        return self.__long

    def get_elev(self):
        return self.__elev

    def get_time(self):
        return self.__time

position = []

contador = 0
for track in list.tracks:
    for segment in track.segments:
        for point in segment.points:
            position.append(puntos(point.latitude, point.longitude, point.elevation, point.time))
            contador+=1

key = "bf20a5bb85774b0c9e9b7b319c92040f"

# for testing
# for i in range(0,18000,1000):
#     print(get_name(position[i].get_lat(), position[i].get_long(), "or" , key))ß
# print all the points lat and long
for i in range(0,1000, 5):
    print('{0} -> Lat/Long: {1},{2} Time: {3} --> Street: {4}'.format(i, position[i].get_lat(), position[i].get_long(), position[i].get_time(), get_name(position[i].get_lat(), position[i].get_long(), )))
