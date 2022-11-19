# the exp() function in python allows users to calc the exponential value with the base set to e.
# how we can use something like a for loop in order to create a func like this on our own.
print(2**3)


def raise_to_power(base_num, pow_num): #inside this function we are taking in 2 parameters/input, a base number and a power number.
    result = 1 # defining variable here called result, is where we are storing the actual result of doing the math
    for index in range(pow_num): # specifying for loop through looping through range of numbers, loop through power number of times
        result = result * base_num # every time through the loop result times base number 
    return result

print(raise_to_power(2, 3))
