#student.py used for classes&objects.py
#within this class e.g. student class, can define a bunch of attributes, use things like strings integers and booleans
class Student: #class of what a student datatype is, object is actual student with name major gpa not just template etc
    def __init__(self, name, major, gpa, is_on_probation): #initialise function, used to map out what attributes a student should have
        # the values passed in above i.e. self, name, major.. are just parameters, u need to take the values you passed in & need to assign them to actual attributes of the object
        self.name = name # name of the student object will be equal to the name we passed in
        self.major = major # name of the student major will be equal to the name we passed in
        self.gpa = gpa # the student's gpa will be equal to the gpa we passed in
        self.is_on_probation = is_on_probation 
        
        
    def on_honor_roll(self):
        if self.gpa >= 6.0:
            return True
        else: 
            return False