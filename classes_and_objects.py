'''
importing a class from file custom_class and using class called Student within it
'''

'''
Can use one of these to just import one class but does not work for multiple imports
for multiple imports you need to import the custom_class and then use custom_class.Student(,,,,) to call the Student and Bot classes
from custom_class import Student
from custom_class import Bot
'''
import custom_class

#john_d will become a Student object using the starting values below, We made (name, major, gpa, and is_on_probation) fields in the custom_class file
john_d = custom_class.Student("john", "engineering", 4.0, False)
student2 = custom_class.Student("sev", "engineering", 3.0, True)
print(john_d.name)
print(student2.name)

#using a second class name bot within custom_class file
bot = custom_class.Bot(1,6)
print(bot.is_on)

#this is a function i created in the student class
print(student2.is_on_honors())
print(john_d.is_on_honors())
