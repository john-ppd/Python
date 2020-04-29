#we use input() and it will prompt the user to type, can se a variable equal to it
name = input("enter you name: ")
age = input("enter your age: ")
print("Your name is " + name + " and you are " + str(age) + " years old, damn you're getting up there")

#making a calculator
num1 = input("Enter a number")
num2 = input("Enter another number")

print(num1 + num2)#THIS IS ERROR, will print 1015 if 10 is num 1 and 15 is num 2. By default inputs are STRINGS, need to convert to numbers.


#Float is how we get decimal values
result = float(num1) + float(num2)
print("float")
print(result)

#RETURNS INT, whole number, will give error if the input is not an int or whole number
result = int(num1) + int(num2)
print(result)