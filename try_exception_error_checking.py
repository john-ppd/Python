'''
try and except are used to catch errors so that instead of breaking your program they just display a line of text and continue one
'''

try:
    #10/0 would make it go directly to the exept line and not do the input command
   # answer = 10/0
    number = int(input("Enter a num"))
    print(number)
#we can use execpt: to catch all possible errors, but it's better to use specific error checks like ZeroDivisionError and ValueError, also can save error as a variable, in this case as cerr and display that variable later
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input because you did not type an INT type")