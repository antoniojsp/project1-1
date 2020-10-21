from getgpx import get_points
from distance import distance
import gpxpy

file = open('09_27_20.gpx', 'r')#just for testing, it won't be here in final version
parseado = gpxpy.parse(file)
list = get_points(parseado)#array of objects that hold information like lat, long, elev, time. It holds all the info from the gpx file, every point (Look up in getgpx.py to see how the class is defined)

#start and end points in the gpx file. This function will roll over each point and calculate the distance of a segment(from one point to another) and add up to give the total distance.
#The way I have organized everything is that the function that detects changes in street will return the index value where this happens and return the index (among the name of the street)  For instance, the route starts in NW Sprouce Ave (index 0,44.587662, -123.256691) and goes to Higland dr (index 88, 44.587414, -123.2624050 and turns right. Now, if we put start = 0 and end = 88), it returns the distance of all the points between that range.

def route_distance(start, end):
    segment = 0
    for i in range(start, end):

        segment+=distance(list[i].get_lat(), list[i].get_long(), list[i+1].get_lat(), list[i+1].get_long())

    return segment

#test
print("{:0.2f}".format(route_distance(0,len(list)-1)))
