number_grid = [
    [1, 2, 3], #row 0 because its the 0 element of the array
    [4, 5, 6], #row 1
    [7, 8, 9], #row 2
    [0]        #row 3 
]

# 4 elements


#how access individual elements inside this 2d list structure 
print(number_grid[0][0]) #in the square brackets, put the index of the row you want to access, then put the index of the column this would be 1

#nested for loop
for row in number_grid:
    for col in row: #each individual column/element inside of the arrays
        print(col) #should print out every single value inside of the array inside of the number grid