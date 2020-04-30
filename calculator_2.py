#when we use the input() commmand by default it will be a string, must convert to float value to have decimal math, can make a function to do this or just wrap each individual input

num1 = float(input("First number"))
operator = (input("pick * + - or /"))
num2 = float(input("Second number"))

def domath(num1, operator, num2):
    if(operator == "*"):
        return num1*num2
    elif(operator == "+"):
        return num1+num2
    elif(operator == "/"):
        return num1/num2
    elif (operator == "-"):
        return num1 - num2
    else:
        return "Invalid operator"

print(domath(num1, operator, num2))