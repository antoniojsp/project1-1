from google import get_name_google
from getgpx import get_points
from distance import distance
import gpxpy
import time

from multiprocessing.pool import ThreadPool#multi process

start_time = time.time()#record time

file = open('09_27_20.gpx', 'r')
parseado = gpxpy.parse(file)
position = get_points(parseado)#array of objects that hold information like lat, long, elev, time.


start = 0#first point
end = len(position)-1#last point
print("Start: {} End:{}".format(start,end))#debug

pool = [""]*len(position)#cache to reduce the number of requests
print(len(pool))

def change(list, start, end, storage):#list with all
    middle = int((start+end)/2)

    pool1 = ThreadPool(processes=1)

    if pool[start] == "":
        async_result = pool1.apply_async(get_name_google, (list[start].get_lat(), list[start].get_long()))
        # pool[start] = get_name_google(list[start].get_lat(), list[start].get_long())
        pool[start] = async_result.get()
    if pool[middle] == "":
        async_result1 = pool1.apply_async(get_name_google, (list[middle].get_lat(), list[middle].get_long()))
        pool[middle] = async_result1.get()
        # pool[middle] = get_name_google(list[middle].get_lat(), list[middle].get_long())
    if pool[end] == "":
        async_result2 = pool1.apply_async(get_name_google, (list[end].get_lat(), list[end].get_long()))
        pool[end] = async_result2.get()
        # pool[end] = get_name_google(list[end].get_lat(), list[end].get_long())

    if pool[start] == pool[middle] and pool[middle] == pool[end]:
        return

    elif (pool[start] == pool[middle] and  pool[middle] != pool[end]) or (pool[start] != pool[middle] and  pool[middle] == pool[end]):

        if pool[middle+1] == "":
            # pool[middle+1] = get_name_google(list[middle+1].get_lat(), list[middle+1].get_long())
            async_result3 = pool1.apply_async(get_name_google, (list[middle+1].get_lat(), list[middle+1].get_long()))
            pool[middle+1] = async_result3.get()
        if pool[middle-1] == "":
            # pool[middle-1] = get_name_google(list[middle-1].get_lat(), list[middle-1].get_long())
            async_result4 = pool1.apply_async(get_name_google, (list[middle-1].get_lat(), list[middle-1].get_long()))
            pool[middle-1] = async_result4.get()

        if pool[middle] != pool[middle-1] or pool[middle] != pool[middle+1]:
            # print("Street now{}".format(pool[middle]))
            if len(storage) == 0:
                # saving.append(Holder(middle, pool[middle-1]))
                if pool[middle-1] not in storage:
                    storage.append((middle,pool[middle-1]))
            else:
                if storage[len(storage)-1][1] == pool[middle-1]:
                    storage.append((middle,pool[middle]))
                else:
                    storage.append((middle,pool[middle-1]))

        else:
            change(list,start, middle, storage)
            change(list, middle, end, storage)
    else:
        change(list,start, middle, storage)
        change(list, middle, end, storage)

intersection = []
change(position, start, end, intersection)
#
# print([str(calles[i.get_index()-1]) +" "+ str(calles[i.get_index()])  +" "+ str(calles[i.get_index()+1]) for i in intersection])
#
j = 0
for i in pool:
    if i != "":
        j+=1
print(j)
# print(pool)

print([i[1] for i in intersection] )

# print([i.get_index() for i in intersection] )
print("--- %s seconds ---" % (time.time() - start_time))
