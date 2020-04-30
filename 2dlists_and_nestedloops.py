list2d = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

#[row][col]
#remember that row one is [0]
print(list2d[3][0])

#NESTED LOOP
#parsing through 2d lists you can use row as a number and it will know how many rows you have

for row in list2d:
    print(row)

for col in list2d:
    print(col)

#use nested loop to print each element individually in 2d list

for row in list2d:
    for col in row:
        print(col)

