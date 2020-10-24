from distance import *
from google import get_name_google
from getgpx import get_points
from nose.tools import *
import gpxpy
import math
from angle import get_angle

#test create object Points, create array and storage in memory all the points.
file = open('09_27_20.gpx', 'r')
parseado = gpxpy.parse(file)
position = get_points(parseado)#array of objects that hold information like lat, long, elev, time.

list = [0,88,123,125,127,574,663,663,704, 1148,1260,1292,1294,1364,1431,1435,1722,2230,2296,2404,3445,3731,4593,5045,5168,5315,5742,6552,6603,6614,6890,8689,8826,8829,8850,8900,8919,8923,8936,8959,9044,9152,9187,9283,9762,9902,9906,10004,10014,10032,10049,10193,10336,10344,10344,10347,10362,10480,10488,10488,10511,11484,12123,12346,12606,12633,13709,13781,13911,13925,13959,13997,14027,14033,14060,14930,14974,15074,15124,15217,15345,16078,16432,16437,16463,17226,17310,17370,17443,17513,17548,17800,18031,18034,18042,18087,18103,18105,18109,18114,18122,18122,18126,18210,18231,18317,18374]

rango = 20


def direction(input):

    rango = 20#how far left and right
    result = []
    turn = ""
    passed = []###
    meters_list = []
    turn_list = []

    print(len(input))
    for i in range(0,len(input)-1):
        degree = 0
        if i == 0:
            degree = 180
        else:
            a = [position[input[i]-rango].get_lat(), position[input[i]-rango].get_long()]
            b = [position[input[i]].get_lat(), position[input[i]].get_long()]
            c = [position[input[i]+rango].get_lat(), position[input[i]+rango].get_long()]
            degree = get_angle(a,b,c)

        if degree < 130.0 or degree > 240.0 or i == 0:
            if i == 0:
                turn = "Start"
            if degree >240:
                turn = "Right"
            elif degree <130:
                turn = "Left"

            passed.append(input[i])
            turn_list.append(turn)

    size = len(passed)
    for i in range(0,size-1):
        temp = passed[i]
        temp1= passed[i+1]
        meters = route_distance(temp, temp1)
        result.append([temp, turn_list[i], meters, position[temp].get_lat(), position[temp].get_long()])

    ending = passed[size-1]
    result.append([size-1, passed[size-1] , "End", 0, position[ending].get_lat(), position[ending].get_long()])
    return result



answer = direction(list)

for i in answer:
    print(i)
