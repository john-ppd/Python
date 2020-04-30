#imports are need for some math function
#Imports are called modules, can find online
from math import *


#We don't need to use a variable type and the variable will support all types, float, double, and other.

x = 50
print(x)

x += 5
print(x)

#modulus operator, will work the same and display remained after integer division, works with decimals too
x = 5.5%2
print(x)

#printing out numbers and string same line need a wrap on the numbers, print(str(numbers)) makes the numbers into string type
numbers = 123
string = "hi there"
print(str(numbers) + string)

#ABSOLUTE VALUE
my_num = -5
print(abs(my_num))

#raised to the power of (pow(variable, power_as_int)), works with negatives
print(pow((my_num), 2))

#MAX number, max(4,5,6) would print out 6
#MIN number, min(4,6,10) would print out 4
print(max(4,5,6))
print(min(4,6,10))

#ROUND function, rounds standard rounding, round(3.51) will print out 4, round(3.49) will output 3
print(round(3.51))
print(round(3.49))

#FLOOR function need math import, it chops off the decimal (rounds down)
#CEIL rounds up
print(floor(3.98))
print(ceil(3.01))

#SQRT
print(sqrt(25))

#EXPONENTS, 2**3 means 2^3
x = 2**3
print(x)

#using a function to raise to powers
def raise_to_power(input, exponent):
    result = 1 #must be tabbed!
    for x in range(exponent):
        result *= input
    return result

print(raise_to_power(3,3))

