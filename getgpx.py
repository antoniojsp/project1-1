import gpxpy
from directions import get_name

file = open('09_27_20.gpx', 'r')
list = gpxpy.parse(file)

class puntos:
    def __init__(self,lat, long, elev):
        self.__lat = lat
        self.__long = long
        self.__elev = elev

    def get_lat(self):
        return self.__lat

    def get_long(self):
        return self.__long

    def get_elev(self):
        return self.__elev

position = []

for track in list.tracks:
    for segment in track.segments:
        for point in segment.points:
            position.append(puntos(point.latitude, point.longitude, point.elevation))
            # print('Point at Lat: {0}, Long: {1}'.format(point.latitude, point.longitude))

for i in position:
    print('Point at Lat: {0}, Long: {1}'.format(i.get_lat(), i.get_long()))

print(len(position))
key = "bf20a5bb85774b0c9e9b7b319c92040f"

for i in range(0,18000,1000):
    print(get_name(position[i].get_lat(), position[i].get_long(), "or" , key))
