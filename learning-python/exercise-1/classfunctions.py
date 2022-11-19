from student import Student

# essentially a class function is a little function that can be used by the objects of the class.

student1 = Student("Matt", "Computer Science", 5.2, False)
student2 = Student("Allie", "Psychology", 6.5, False)
student3 = Student("Vivian", "Medicine", 6.9, False)
    
print(student1.on_honor_roll())
print(student2.on_honor_roll())
print(student3.on_honor_roll())
