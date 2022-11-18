# better calculator than before, will be able to do all the basic arithmetic calculations and allow users to specify what number and operation
# uses if statements

num1 = float(input("Enter first number: "))
op = input("Enter operator ")
num2 = float(input("Enter second number number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")
    
