#FINDS THE TURNING POINTS, IT RETURNS THE NAMES AND THE NUMBER OF THE INDEX WHERE THE TURNS ARE.
#it gets the info  from the points from the gpx files and perform a recursion search
#to get the points where the streets changes. used the module "google" from where it connects to google
#maps and get the name of the address where some point (lat,long) is located.
#returns and 2d Array witht [gpx index number, name of streets, latitude, longitud]
#latest version (10/20/20)
import googlemaps
import json
from google import get_name_google
from getgpx import *
import gpxpy
import math
from math import cos, sin, asin, radians, sqrt

# from distance import distance
from multiprocessing.pool import ThreadPool#multi process
# import threading
# from multiprocessing import Process#to run concurrently.

#Class will return 2d array with the result of the route
class Route:

    def __init__(self, list):
        self.__arr = []#The points from the gpx live here.
        for i in list:
            self.__arr.append(i)#filling up __arr with the points from the gpx file
        self.__pool = [""]*len(list)#cache to reduce the number of requests, collisions will prevent requesting more data.
        self.__storage = []#partial results go here.

    def request(self,parts):#extract points, get the name address and add the info into the pool array(cache)
        thpool = ThreadPool(processes=1)#running concurrently
        interpolate = [""]*len(parts)# can request a list of requests.

        for i in parts:
            if self.__pool[i[1]] == "":#if the data is in the cache array, it will not request the data but use the one from the pool array
                async_result = thpool.apply_async(get_name_google,(self.__arr[i[1]].get_lat(), self.__arr[i[1]].get_long()))
                interpolate[i[0]] = async_result.get()#holds more than one request.
                self.__pool[i[1]] = interpolate[i[0]]

    

    def add_point(self, index):#for the first and last point:
        self.__storage.append([index, get_name_google(self.__arr[index].get_lat(), self.__arr[index].get_long()), self.__arr[index].get_lat(), self.__arr[index].get_long()])

    def change(self, start, end):#list contains all the points, start first point, end last one and storage saves the results.
        middle = int((start+end)/2)

        parts1 = [[0,start],[1,middle],[2,end]]
        self.request(parts1)

        # base case: when  the start, the middle and the end is the same.
        if self.__pool[start] == self.__pool[middle] and self.__pool[middle] == self.__pool[end]:
            return

        # when start and middle are equal and middle and end not equal(or viceverse), possible indication of a point of change.
        if (self.__pool[start] == self.__pool[middle] and  self.__pool[middle] != self.__pool[end]) or (self.__pool[start] != self.__pool[middle] and  self.__pool[middle] == self.__pool[end]):

            parts2 = [[0,middle+1], [1,middle-1]]
            self.request(parts2)

            #checks if the next point from the middle is different, if it is, change detected and added.
            if  self.__pool[middle-1] != self.__pool[middle]:
                self.__storage.append([middle-1, self.__pool[middle-1], self.__arr[middle-1].get_lat(), self.__arr[middle-1].get_long()])
            elif self.__pool[middle] != self.__pool[middle+1]:
                self.__storage.append([middle, self.__pool[middle], self.__arr[middle].get_lat(), self.__arr[middle].get_long()])
            else:
                self.change(start, middle)
                self.change(middle+1, end)

        else:
            parts3 = [[0,middle+1], [1,middle-1]]
            self.request(parts3)
            #checks when start, middle and end are different but the middle falls exactly in a changing point. it will perform the checking and add the point if it falls in the changing point.
            if self.__pool[middle-1] != self.__pool[middle]:
                self.__storage.append([middle-1, self.__pool[middle-1], self.__arr[middle-1].get_lat(), self.__arr[middle-1].get_long()])
            elif self.__pool[middle] != self.__pool[middle+1]:
                self.__storage.append([middle, self.__pool[middle], self.__arr[middle].get_lat(), self.__arr[middle].get_long()])
            #will continue dividing and searching.
            self.change(start, middle)
            self.change(middle+1, end)

    #from math formula
    # def get_angle(self, before, center, after):
    #     ang = math.degrees(math.atan2(after[1]-center[1], after[0]-after[0]) - math.atan2(before[1]-center[1], before[0]-center[0]))
    #     result = ang + 360 if ang < 0 else ang
    #     return result

    #rolls through the index from one point to another and add up the distances betweeen those points.
    def route_distance(self, start, end):
        segment = 0
        for i in range(start, end):
            segment+=distance(self.__arr[i].get_lat(), self.__arr[i].get_long(), self.__arr[i+1].get_lat(), self.__arr[i+1].get_long())
        return segment


    def direction(self,input):#array of indexes

        result = []#holds all the information
        turn = ""
        rango = 20
        result.append([])#2d array to hold addreses, distance, turning, index
        for i in range(0,len(input)-1):
            degree = 0
            if i == 0:
                degree = 180
            else:
                #get_angle needs 3 list arguments to figure out the angle of the turn to detect if it goes right or left.
                a = [self.__arr[input[i]-rango].get_lat(), self.__arr[input[i]-rango].get_long()]
                b = [self.__arr[input[i]].get_lat(), self.__arr[input[i]].get_long()]
                c = [self.__arr[input[i]+rango].get_lat(), self.__arr[input[i]+rango].get_long()]
                degree = self.get_angle(a,b,c)

            #if angle lower of 130 and higher than 240, we could assume that is a turn
            #this function use as an input, one array of index with those possible turning points.
            #using this range, we can detect the falses positives
            if degree < 130 or degree > 240 or i == 0:
                if degree >240:
                    turn = "Right"
                if degree <130:
                    turn = "Left"

                meters = self.route_distance(input[i], input[i+1])

                result.append([input[i], turn, meters, get_name_google( self.__arr[input[i]].get_lat(), self.__arr[input[i]].get_long()), self.__arr[input[i]].get_lat(), self.__arr[input[i]].get_long() ])

        return result

    #it rolls through the array and add distances from one index to another. Those indexes are the turning points and we assume that belongs to the same street
    # def route_distance(self,start, end):
    # 	segment = 0
    # 	for i in range(start,end):
    # 		segment+=self.distance(self.__arr [i].get_lat(), self.__arr [i].get_long(), self.__arr [i+1].get_lat(), self.__arr [i+1].get_long())
    # 	return segment

    #get angle
    def get_angle(self,a, b, c):
        angular = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
        return angular + 360 if angular < 0 else angular

    def distance(self,ini_lat, ini_lon, fin_lat, fin_lon):
    	dif_lat = radians(ini_lat) - radians(fin_lat)
    	dif_lon = radians(ini_lon) - radians(fin_lon)
    	earth_radio = 6371 #radius in km
    	distance = (sin(dif_lat/2))**2 + cos(radians(ini_lat)) * cos(radians(fin_lat)) * (sin(dif_lon/2))**2
    	distancia = earth_radio * asin(sqrt(distance)) * 2 * 1000 # multiply by 1000 to convert to 	distance in meters
    	return distancia


    def result(self):
        self.add_point(0)
        end = len(self.__arr)-2
        self.change(0, end)
        self.add_point(end+1)#add first and last points to indicate the start and the end
        self.__storage.sort(key=lambda x: x[0])#sort order

        # print(self.__storage)

        i = 0
        index = []
        while i < len(self.__storage)-1:
            j=0
            while j < len(self.__storage[i])-1:
                if j == 0:
                    try:
                        index.append(self.__storage[i][j])
                    except:
                        pass
                j+=1
            i+=1

        final = self.direction(index)#put things everything together.

        return final
