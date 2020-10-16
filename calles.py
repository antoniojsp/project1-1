#experiment for binary search
calles = [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,6,6,6,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8 ]
# [0,0,0,1,1,1,1,2,2,2,2,3,3,3,3] 0 7 14
# [0,0,0,1,1,1,1,2]0 3 7 | [2,2,2,3,3,3,3]8 11 14
# [0,0,0,1]0 1 3 [1,1,1,2] 4 5 7  [2,2,2,3] [3,3,3]
# -[0,0]0 1 1 *[0,1]2 2 3 | -[1,1]4 5 5 *[1,2]6 6 7| -[2,2]8 8 9 *[2,3]10 10 11 |-[3,3]12 12 13 -[3]14
#  [0,1]2 2 3  | *[1,2]6 6 7 | *[2,3]10 10 11

#check if star, end and middle are different, if they are, divided
#if star==middle or middle == end, check middle+1 and middle-1, if differemt, return middle.

# tail recursions
# sugar coarting
# pattern matching
# algebraic database and pattern matching

start = 0
end = len(calles)-1
print("end {}".format(end))
def change(list, start, end):
    middle = int((start+end)/2)
    # print("Start: {} middle: {} end:{}".format(start,middle,    end))
    # print([list[i] for i in range(start,end+1)])
    #
    if list[start] == list[middle] and  list[middle] == list[end]:
        return
    elif (list[start] == list[middle] and  list[middle] != list[end]) or (list[start] != list[middle] and  list[middle] == list[end]):
        if list[middle]!=list[middle+1] or list[middle]!=list[middle-1]:
            print("--->  value: {} index: {}".format(list[middle],middle))
        else:
            change(list,start, middle)
            change(list, middle, end)
    else:
        change(list,start, middle)
        change(list, middle, end)

# [0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,7,7,7,8,8,8]0 48
# [0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3]0 24  [3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,7,7,7,8,8,8]25 48


change(calles, 0, end)
