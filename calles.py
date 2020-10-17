#experiment for binary search
calles = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9 ]


lista_calles = ["NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland",'NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd']


# [0,0,0,1,1,1,1,2,2,2,2,3,3,3,3] 0 7 14
# [0,0,0,1,1,1,1,2]0 3 7 | [2,2,2,3,3,3,3]8 11 14
# [0,0,0,1]0 1 3 [1,1,1,2] 4 5 7  [2,2,2,3] [3,3,3]
# -[0,0]0 1 1 *[0,1]2 2 3 | -[1,1]4 5 5 *[1,2]6 6 7| -[2,2]8 8 9 *[2,3]10 10 11 |-[3,3]12 12 13 -[3]14
#  [0,1]2 2 3  | *[1,2]6 6 7 | *[2,3]10 10 11

#check if star, end and middle are different, if they are, divided
#if star==middle or middle == end, check middle+1 and middle-1, if differemt, return middle.

class Holder:
    def __init__(self, index,value):
        self.__index = index
        self.__value = value
    def get_index(self):
        return self.__index
    def get_value(self):
        return self.__value

intersection = []

start = 0
end = len(lista_calles)-1

def change(list, start, end, saving):
    middle = int((start+end)/2)

    if list[start] == list[middle] and  list[middle] == list[end]:
        return
    elif (list[start] == list[middle] and  list[middle] != list[end]) or (list[start] != list[middle] and  list[middle] == list[end]):
        if list[middle]!=list[middle+1] or list[middle]!=list[middle-1]:
            if len(saving) == 0:
                saving.append(Holder(middle, list[middle-1]))
            else:
                if saving[len(saving)-1].get_value() == list[middle]:
                    saving.append(Holder(middle, list[middle]))
                else:
                    saving.append(Holder(middle, list[middle-1]))

        else:
            change(list,start, middle, saving)
            change(list, middle, end, saving)
    else:
        change(list,start, middle, saving)
        change(list, middle, end, saving)

change(lista_calles, 0, end, intersection)

# print([str(calles[i.get_index()-1]) +" "+ str(calles[i.get_index()])  +" "+ str(calles[i.get_index()+1]) for i in intersection])



print([i.get_value() for i in intersection] )
print([i.get_index() for i in intersection] )
