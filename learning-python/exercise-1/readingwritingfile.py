
employee_file = open("employees.txt", "r") #R AND W
for employee in employee_file.readlines():
    
    print(employee_file.readable())

    print(employee_file.read())

    print(employee_file.readlines())

employee_file.close()

# confused practise more


#writing new files and appending onto new files
employee_file = open("employees.txt", "a") #appending, adding text to the file, if you use W it will over write the file not add onto it
employee_file.write("\nToby - Human Resources")

employee_file.close