import gpxpy
from getgpx import get_points

# file = open('09_27_20.gpx', 'r')
# parseado = gpxpy.parse(file)
# position = get_points(parseado)#array of objects that hold information like lat, long, elev, time.

with open("Untitled.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

list=[]
for i in content:
    if i != "":
        temp = (i.replace(']', ''))
        temp1= (temp.replace('[', ''))
        # temp2 = (temp1.replace(',', ''))
        # parte = (temp1.replace(',', ''))
        # print(parte)
        numero = temp1.split(",")
        # print(numero)
        list.append(numero)

for i in list:
    print("{},{}\n".format(i[2],i[3]),end=" ")
    # print(i)
