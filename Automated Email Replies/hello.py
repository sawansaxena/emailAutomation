def my_function():
    print("hello world")
    
name ="nickolas"

# Defining a class
class Student:
    def __init__(self, name, course):
        self.course = course
        self.name = name

    def get_student_details(self):
        print("Your name is " + self.name + ".")
        print("You are studying " + self.course)