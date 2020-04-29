
array1 = ["kevin","james","john", "jim", "raynor"]
print(array1[1])
#NEGATIVES, if we use -1 we will get the last item, -2 will get jim -3 will get
print(array1[-1])
print((array1[-2]))

#PRINT RANGE
#[1:] will print from 1 -> end
#[1:3] will print [1] and [2]
#[1:4] will print [1] [2] [3]

print(array1[1:])
print(array1[1:3])
print(array1[1:4])

print(array1)
array1[1] = "changed name"
print(array1)

#Working with lists
array1 = ["kevin","james","john", "jim", "raynor"]
array2 = [1,4,6,7,8]

#.extend will add all values from one array to another
#array 2 will be added onto the end of array1
array1.extend(array2)
print(array1)

#.append will add an item onto the end of the list
array1.append("added to end of array 1")
print(array1)

#.insert(at what array location, "value to add")
#INSERT data into an array location and shift all others down  by 1
array2.insert(1,"inserted at [1]")
print(array2)

#removing elements
array2.remove("inserted at [1]")
print(array2)
#REMOVE ALL
array2.clear()
print("array 2 is empty")
print(array2)

#REMOVE LAST ELEMENT using .pop()
array2 = [1,4,6,7,8]
print(array2)
array2.pop()
print(array2)

#SEARCHING LIST FOR ELEMENT, will return the array location for the given search entry, if does not find will result in error
print(array2.index(4))

#Count how many elements of something are in a list
array2 = [1,4,4,5,4,4,4,4,6,7,8]
print(array2.count(4))

#SORT LIST, will put string in alphabetical order and numbers from low -> high
array2.sort()
print(array2)
array1 = ["kevin","james","john", "jim", "raynor"]
print(array1)
array1.sort()
print(array1)

#SORT LIST high->low
array1.reverse()
array2.reverse()
print(array1)
print(array2)

#copy lists, will get all attributes of other list
array3 = array1.copy()
print("array 3")
print(array3)


