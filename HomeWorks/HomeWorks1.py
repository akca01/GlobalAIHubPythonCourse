# Homework - 1:

# First Point
list1 = [1,3,5,7,9]
list2 = [0,2,4,6,8,10]
# Second Point
newList = []
newList.extend(list1)
newList.extend(list2)
newList.sort()
newList = [i * 2 for i in newList]
# Third Point
for i in newList:
    print(i, type(i))







