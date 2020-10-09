from distance import distance
from directions import get_name_tamu
from google import get_name_google
from getgpx import get_points
import gpxpy

#two points
#janeth smith house
inicio_lat =  44.046074#degrees in decimals
inicio_lon = -122.932640
#7-11
final_lat =  44.040276
final_lon = -123.080187

file = open('09_27_20.gpx', 'r')
parseado = gpxpy.parse(file)

# print ("{:.2f} meters".format(distance(inicio_lat, inicio_lon, final_lat, final_lon)))

position = get_points(parseado)

#test gpx
for i in range(0,1000, 5):
    print('{0} -> Lat/Long: {1},{2}--> Street: {3}'.format(i, position[i].get_lat(), position[i].get_long(), get_name_google(position[i].get_lat(), position[i].get_long())))
