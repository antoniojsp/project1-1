from google import get_name_google
from getgpx import get_points
from distance import distance
import gpxpy

file = open('09_27_20.gpx', 'r')
parseado = gpxpy.parse(file)
position = get_points(parseado)#array of objects that hold information like lat, long, elev, time.

class Holder:
    def __init__(self, index, name):
        self.__index = index
        self.__name = name
    def get_index(self):
        return self.__index
    def get_name(self):
        return self.__name

start = 0
end = len(position)-1
print("Start: {} End:{}".format(start,end))

pool = [""]*len(position)

def change(list, start, end, saving):
    middle = int((start+end)/2)

    if pool[start] == "":
        pool[start] = get_name_google(list[start].get_lat(), list[start].get_long())
    if pool[middle] == "":
        pool[middle] = get_name_google(list[middle].get_lat(), list[middle].get_long())
    if pool[end] == "":
        pool[end] = get_name_google(list[end].get_lat(), list[end].get_long())

    if pool[start] == pool[middle] and pool[middle] == pool[end]:
        return

    elif (pool[start] == pool[middle] and  pool[middle] != pool[end]) or (pool[start] != pool[middle] and  pool[middle] == pool[end]):

        if pool[middle+1] == "":
            print(middle+1)
            pool[middle+1] = get_name_google(list[middle+1].get_lat(), list[middle+1].get_long())
        if pool[middle-1] == "":
            pool[middle-1] = get_name_google(list[middle-1].get_lat(), list[middle-1].get_long())

        if pool[middle] != pool[middle-1] or pool[middle] != pool[middle+1]:
            # print("Street now{}".format(pool[middle]))
            if len(saving) == 0:
                saving.append(Holder(middle, pool[middle-1]))
            else:
                if saving[len(saving)-1].get_name() == pool[middle-1]:
                    saving.append(Holder(middle, pool[middle]))
                else:
                    saving.append(Holder(middle, pool[middle-1]))

        else:
            change(list,start, middle, saving)
            change(list, middle, end, saving)
    else:
        change(list,start, middle, saving)
        change(list, middle, end, saving)

intersection = []
change(position, start, end, intersection)
#
# print([str(calles[i.get_index()-1]) +" "+ str(calles[i.get_index()])  +" "+ str(calles[i.get_index()+1]) for i in intersection])
#
print([i.get_name() for i in intersection] )
# print([i.get_index() for i in intersection] )
