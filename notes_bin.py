#experiment for binary search
calles = [0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4]#0 13 27

#(if start != middle != end) divide
#[0,0,0,0,1,1,1|,1,1,1,1,2,2,2] 0 6 13  [2,2,2,2,3,3,3|,3,3,3,4,4,4,4] 14 20 27

#if start == middle or middle == end, check middle+1 and middle-1, if middle != middle+1 or -1, then return middle
# *[0,0,0,0|,1,1,1]0 3 6 *[1,1,1,1|,2,2,2] 7 10 13 *[2,2,2,2|,3,3,3]14 17 20  *[3,3,3,4|,4,4,4] 21 24 27


calles = [0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,3]#0 7 15

# [0,0,0,1|,1,1,1,2]0 3 7     *[2,2,2,3|,3,3,3,3]8 11 15
# [0,0|,0,1]0 1 3  [1,1|,1,2]4 5 7
# - [0,0]0 1 1 *[0,1] 2 2 3  -[1,1]4 4 5 *[1,2]6 6 7



#[0,0,0,0,0,0|,0,0,0,0,1]0 5 10
#-[0,0,0,0,0,0]0 2 5   [0,0,0|,0,1]6 8  10
# -[0,0,0]6 7 8  *[0,1] 9 9 10

#check if star, end and middle are different, if they are, divided
#if star==middle or middle == end, check middle+1 and middle-1, if differemt, return middle.
