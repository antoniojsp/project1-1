from distance import *
from google import get_name_google
from getgpx import get_points
from nose.tools import *
import gpxpy
import math

#test create object Points, create array and storage in memory all the points.
file = open('09_27_20.gpx', 'r')
parseado = gpxpy.parse(file)
position = get_points(parseado)#array of objects that hold information like lat, long, elev, time.


def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

list = [0,88,123,125,127,574,663,663,704,1148,1260,1292,1294,1364,1431,1435,1722,2230,2296,2404,3445,3731,4593,5045,5168,5315,5742,6552,6603,6614,6890,8689,8826,8829,8850,8900,8919,8923,8936,8959,9044,9152,9187,9283,9762,9902,9906,10004,10014,10032,10049,10193,10336,10344,10344,10347,10362,10480,10488,10488,10511,11484,12123,12346,12606,12633,13709,13781,13911,13925,13959,13997,14027,14033,14060,14930,14974,15074,15124,15217,15345,16078,16432,16437,16463,17226,17310,17370,17443,17513,17548,17800,18031,18034,18042,18087,18103,18105,18109,18114,18122,18122,18126,18210,18231,18317,18374]

rango = 20
# for i in list:
#     print("{},{}".format(position[i].get_lat(),position[i].get_long()))
result = []
result.append([])
for i in list:
    print("{},{}".format(position[i].get_lat(),position[i].get_long()))

print(len(list))
for i in range(0,len(list)-1):
    degres = getAngle((position[list[i]-rango].get_lat(),position[list[i]-rango].get_long()), (position[list[i]].get_lat(),position[list[i]].get_long()), ( position[list[i]+rango].get_lat(),position[list[i]+rango].get_long()))

    if degres < 120.0 or degres > 240.0:
        if degres < 180:
            direction = "Left"
        else:
            direction = "Right"
        meters = route_distance(list[i],list[i+1])
        print("{} {}".format(list[i],list[i+1]))
        result.append([[list[i]],[degres],[direction],[meters],[position[list[i]].get_lat()],[position[list[i]].get_long()],[]])


    # result.append(get_name_google(position[list[i]].get_lat(), position[list[i]].get_long()))
# for i in range(0,len(list)-2):
#     meters = route_distance(list[i],list[i+1])
#     result[i].append(meters)
#
# for i in result:
#     # print("{},{}".format(i[0],i[0]))
#     print("{},{}".format(i[3],i[4]))



    # print("{}:   {} - > {},{} ->{}".format(direction, degres,position[list[i]].get_lat(),position[list[i]].get_long(), get_name_google(position[list[i]].get_lat(), position[list[i]].get_long())))

#
# print(getAngle((44.587662,-123.256691), (44.58762,-123.256981), ( 44.587589,-123.257622)))

# #test search an specific point by index
# # number = 8770
# # lat = position[number].get_lat()
# # long = position[number].get_long()
# # print(get_name_google(lat, long))
#
# #set range from where we want to get points.
# start = 0
# end = len(position)-1
# #prints points from the gpx or points and names. uncomment to change the result.
# for i in range(80,90):
#     # print("location{0}= [{1},{2}]".format(i-70, position[i].get_lat(), position[i].get_long()))
#     # line.append([position[i].get_lat(), position[i].get_long()])
#     print("{0}:  {1},{2}".format(i, position[i].get_lat(), position[i].get_long()))
#     # print('{0} -> Lat/Long: {1},{2}--> Street: {3}'.format(i, position[i].get_lat(), position[i].get_long(), get_name_google(position[i].get_lat(), position[i].get_long())))
