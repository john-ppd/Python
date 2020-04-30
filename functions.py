#FUNCTIONS - to write a function we must say "def" prior to making the function

#def first_function(): makes a function called first_function(), we need to indent the next line. All indented line will be inn the function, first non-indented line breaks out of the function

def first_function():
    print("this is in function")
    print("this is in function")
    print("this is in function")
print("this is NOT in function")

first_function()
#in python if you have only two works you can leave out the _ and no caps
def sayhi(user_name):
    print("hello " + user_name)

sayhi("john")

def add_numbers(a, b, c):
    sum = a+b+c
    print(sum)
add_numbers(1.3,2,13)

#remember if you use a string and then an int in a print statement you must wrap the number in a str() tag

#RETURN STATEMENTS
def cube(user_number):
    return pow(user_number,3)
#NOTHING AFTER RETURN IS EXECUTED
print(cube(9))

store_in_variable = cube(3)
print(store_in_variable)