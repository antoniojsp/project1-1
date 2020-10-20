from google import get_name_google
from getgpx import get_points
from distance import distance
from multiprocessing.pool import ThreadPool#multi process
import gpxpy
import time
import threading

from multiprocessing import Process

#FINDS THE TURNING POINTS, IT RETURNS THE NAMES AND THE NUMBER OF THE INDEX WHERE THE TURNS ARE.

start_time = time.time()#record time
#get the points from the gpx file
file = open('09_27_20.gpx', 'r')
parseado = gpxpy.parse(file)
list = get_points(parseado)#array of objects that hold information like lat, long, elev, time.

#first point and last one that are in the range is verify
start = 0#first point
end = len(list)-1#last point
print("Start: {} End:{}".format(start,end))#debug

pool = [""]*len(list)#cache to reduce the number of requests
intersection = []


def points(parts):
    thpool = ThreadPool(processes=1)
    interpolate = [""]*3

    for i in parts:
        if pool[i[1]] == "":
            async_result = thpool.apply_async(get_name_google,(list[i[1]].get_lat(), list[i[1]].get_long()))
            interpolate[i[0]] = async_result.get()
            pool[i[1]] = interpolate[i[0]]

#adding starting point of the whole road
intersection.append([start, get_name_google(list[start].get_lat(), list[start].get_long()), list[start].get_lat(), list[start].get_long()])

def change(start, end, storage):#list contains all the points, start first point, end last one and storage saves the results.
    middle = int((start+end)/2)

    parts1 = [[0,start],[1,middle],[2,end]]
    points(parts1)

    if pool[start] == pool[middle] and pool[middle] == pool[end]:
        return

    if (pool[start] == pool[middle] and  pool[middle] != pool[end]) or (pool[start] != pool[middle] and  pool[middle] == pool[end]):


        parts2 = [[0,middle+1], [1,middle-1]]
        points(parts2)

        if  pool[middle-1] != pool[middle]:
            storage.append([middle-1, pool[middle-1], list[middle-1].get_lat(), list[middle-1].get_long()])
        elif pool[middle] != pool[middle+1]:
            storage.append([middle, pool[middle], list[middle].get_lat(), list[middle].get_long()])
        else:
            change(start, middle, storage)
            change(middle+1, end, storage)

    else:
        parts3 = [[0,middle+1], [1,middle-1]]
        points(parts3)


        if pool[middle-1] != pool[middle]:
            storage.append([middle-1, pool[middle-1], list[middle-1].get_lat(), list[middle-1].get_long()])
        elif list[middle] != list[middle+1]:
            storage.append([middle, pool[middle], list[middle].get_lat(), list[middle].get_long()])

        change(start, middle, storage)
        change(middle+1, end, storage)

#calling fuction, returns one list of array
change(start, end, intersection)

#adding ending point
intersection.append([end, get_name_google(list[end].get_lat(), list[end].get_long()), list[end].get_lat(), list[end].get_long()])

print([pool[i] for i in range(start,end)])
j = 0
for i in pool:
    if i != "":
        j+=1
print(j)
print(len(intersection))

intersection.sort(key=lambda x: x[0])#sort order

for i in intersection:
    print("{}\n ".format(i))

print("--- %s seconds ---" % (time.time() - start_time))
