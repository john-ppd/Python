is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are a tall female")
elif not(is_male) and not(is_tall):
    print("You are a short female")

def max_num(num1, num2, num3):
    if num1 >= num2 and num2 >= num3:
        return num1
    if num2 >= num1 and num1 >= num3:
        return num2
    if num3 >= num2 and num2 >= num1:
        return num3

print(max_num(3,7,2))