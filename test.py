from distance import distance
from directions import get_name_tamu
from goo import get_name_google
from getgpx import get_points
from nose.tools import *
import gpxpy

# #test distance examples
# example1 = [ 44.588692,-123.268276,44.588787,-123.262550]#  457.48 meters  west east
# result_distance1 = 457.48
# example2 = [ 44.578722,-123.283039, 44.575484,-123.277778]#549.37 meters diagonal
# result_distance2 = 549.37
# example3 = [ 44.577155, -123.292407, 44.577111,-123.283148]#732.37 metes west east
# result_distance3 = 732.37
# example4 = [ 44.077009, -123.047404, 44.063810,-123.048803]#1474.25 meters north and south
# result_distance4 = 1474.25
#
# delta = 10.0 #tolerence in distance 10 meteres plus or less
# # #test distancia
# print ("{:.2f} meters".format(distance(example1[0], example1[1], example1[2], example1[3])))
# assert_almost_equal(distance(example1[0], example1[1], example1[2], example1[3]),result_distance1, delta=delta)
# print ("{:.2f} meters".format(distance(example2[0], example2[1], example2[2], example2[3])))
# assert_almost_equal(distance(example2[0], example2[1], example2[2], example2[3]),result_distance2, delta=delta)
# print ("{:.2f} meters".format(distance(example3[0], example3[1], example3[2], example3[3])))
# assert_almost_equal(distance(example3[0], example3[1], example3[2], example3[3]),result_distance3, delta=delta)
# print ("{:.2f} meters".format(distance(example4[0], example4[1], example4[2], example4[3])))
# assert_almost_equal(distance(example4[0], example4[1], example4[2], example4[3]),result_distance4, delta=delta)

#test create object Points, create array and storage in memory all the points.
file = open('09_27_20.gpx', 'r')
parseado = gpxpy.parse(file)
position = get_points(parseado)#array of objects that hold information like lat, long, elev, time.

import math

def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

list = [0,88,124,574,663,704,1148,1208,1223,1256,1260,1292,1294,1328]

for i in range(1,len(list)-1):
    print(list[i])
    print(getAngle((position[list[i]-15].get_lat(),position[list[i]-15].get_long()), (position[list[i]].get_lat(),position[list[i]].get_long()), ( position[list[i]+105].get_lat(),position[list[i]+15].get_long())))

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
