#

#the init will allow you to define what variable types the class will have, in this case its for a student so we have grades and other

class Student:
#beside (self) we add in other data type parameters
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


    def is_on_honors(self):
        if self.gpa > 3.5:
            return True
        else:
            return False
'''
FUNCTIONS IN CLASS
must have (self) element
now can use student1.is_on_honors call will this class
'''
def is_on_honors(self):
    if self.gpa > 3.5:
        return True

class Bot:
    def __init__(self, is_on, apm):
        self.is_on = is_on
        self.apm = apm

