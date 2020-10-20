#experiment for divide and conquer approach to find the turnings points in the map. NO PART OF THE IMPLEMENTATION

calles = ["NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Spruce","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland","NW Highland",'NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','Hoffman Rd','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Crescent Valley Dr','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Lewisburg Ave','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd','NW Sulphur Springs Rd']


turns = []
start = 0
# calles = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2,1,1,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6]
#[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3, 3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6]0 33 66 == 67

#[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1, 2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3]0 16 33 ==34
#[3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4 ,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6]34 50 66 ==33

#[0,0,0,0,0,0,0,0,0 ,0,1,1,1,1,1,1,1]0 8 16 [2,2,2,2,2,2,2,3,3 ,3,3,3,3,3,3,3,3]17 25 33
#[3,3,3,3,3,3,3,3,3 ,3,3,3,4,4,4,4,4]34 42 50 [4,4,4,4,4,5,5,5, 5,5,5,6,6,6,6,6]51 58 66

# -[0,0,0,0,0 ,0,0,0,0]0 4 8 [0,1,1,1 ,1,1,1,1]9 12 16 [2,2,2,2,2 ,2,2,3,3]17 21 25 -[3,3,3,3, 3,3,3,3]26 29 33
# - [3,3,3,3,3 ,3,3,3,3]34 38 42 **[3,3,3,4, | 4,4,4,4]43 46 50 [4,4,4,4 ,4,5,5,5]51 54 58 **[5,5,5,6 | ,6,6,6,6]59 62 66

# **[0,1,| 1,1]9 10 12  -[1,1,1,1]13 14 16 -[2,2,2,2,2]17 19 21 **[2,2, | 3,3]22 23 25
# -[4,4,4,4]51 52 54 **[4,5, | 5,5]55 56 58 [5,5,5,6]59 60 62 -[6,6,6,6]63 64 66

# -[5,5]59 59 60 **[5,6]61 61 62

#10
end = len(calles)-1
def change(list, start, end, saving):
    middle = int((start+end)/2)

    if list[start] == list[middle] and  list[middle] == list[end]:
        return

    if (list[start] == list[middle] and  list[middle] != list[end]) or (list[start] != list[middle] and  list[middle] == list[end]):

        if  list[middle-1] != list[middle]:
            saving.append([middle-1, list[middle-1]])
        elif list[middle] != list[middle+1]:
            saving.append([middle, list[middle]])
        else:
            change(list,start, middle, saving)
            change(list, middle+1, end, saving)
    else:
        if list[middle-1] != list[middle]:
            saving.append([middle-1, list [middle-1]])
        elif list[middle] != list[middle+1]:
            saving.append([middle, list [middle]])

        change(list,start, middle, saving)
        change(list, middle+1, end, saving)


for i, j in zip(calles, range(0,len(calles))):
    print("{0} {1}".format(j,i))

change(calles, start, end, turns)
turns.sort(key=lambda x: x[0])#sort order
print([i for i in turns])

i=0
while i < len(turns):
    if turns[i][0] == turns[i-1][0]:
        turns.pop(i)
        i-=1
    i+=1

print([i for i in turns])
