# Building a basic calculator using python and user input. Get 2 numbers from a user and then we will add the numbers together and print them on the screen.
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
# result = num1 + num2
# not done yet, have to convert the string to a number, so we have to make the num1 num2 vars into numbers
# result = int(num1) + int(num2)
# print(result)
# does not work with decimals yet so lets fix that, this is because int function looks for integers (whole numbers without decimals) thus
# when you put decimals it will break the program - lets fix that

result = float(num1) + float(num2)
print(result)



