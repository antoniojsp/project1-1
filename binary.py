
from getgpx import get_points
from google import get_name_google

import gpxpy

file = open('09_27_20.gpx', 'r')
parseado = gpxpy.parse(file)
position = get_points(parseado)

rango = []

inicio = 0
final = 100

for i in range(inicio,final):
    rango.append(position[i])

for i in range(0,final-inicio):
    print('{0} -> Lat/Long: {1},{2}--> Street: {3}'.format(i, rango[i].get_lat(), rango[i].get_long(), get_name_google(rango[i].get_lat(), rango[i].get_long())))
