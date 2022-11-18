# special statement that you can use inside a function to send the functions result back to the caller
def cube(num):
   return num * num * num
    
result = cube(4)
print(result)
print(cube(3))