#experiment for binary search
calles = [0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4]

#check if star, end and middle are different, if they are, divided
#if star==middle or middle == end, check middle+1 and middle-1, if differemt, return middle.

start = 0
end = len(calles)-1

# [0,0,0,1|,1,1,1,2]0 3 7     *[2,2,2,3|,3,3,3,3]8 11 15
# [0,0|,0,1]0 1 3  [1,1|,1,2]4 5 7
# - [0,0]0 1 1 *[0,1] 2 2 3  -[1,1]4 4 5 *[1,2]6 6 7

#[0,0,0,0,0,0|,0,0,0,0,1]0 5 10
#-[0,0,0,0,0,0]0 2 5   [0,0,0|,0,1]6 8  10
# -[0,0,0]6 7 8  *[0,1] 9 9 10

def change(list, start, end):

    middle = int((start+end)/2)

    if list[start] == list[middle] and  list[middle] == list[end]:
        return
    elif (list[start] == list[middle] and  list[middle] != list[end])        or (list[start] != list[middle] and  list[middle] == list[end]):
        if list[middle]!=list[middle+1] or list[middle]!=list[middle-1]:
            print(middle)
    else:
        change(list,start, middle)
        change(list, middle+1, end)

change(calles, 0, len(calles)-1)
