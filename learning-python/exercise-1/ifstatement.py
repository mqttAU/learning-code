# I wake up
# If I'm hungry (condition true or false)
    # I eat breakfast (action)
    
# I leave my house
# if it's cloudy
    # I bring an umbrella
# otherwise
    # I bring sunglasses
    
#Im at a restaurant
#if I want meat
    #I order a steak
#otherwise if I want pasta
    #I order spaghetti and meatballs
#otherwise
    #I order a salad

#simple if statement using boolean variables
is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")



if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not male and not tall")
    
    
# if statements and comparisons, instead of using boolean vars can compare different values (numbers, strings)

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300, 40, 5))

# some comparison operators are != means not equal, == equal, >= greater than or equal, <= smaller than or equal




