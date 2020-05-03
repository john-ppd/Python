#since the file my_list.txt is in the same folder as this file, I can simply call it without a complete path

#there are different modes when you open a file, read will only let you read but not modify, write is you write, append you can only add to a value, r+ lets you read and write. read = r, write = w, append = a, r+

#this will read the file, we want to store the text in a variable
my_list = open("my_list.txt", "r")
#it is a good first step to check if a file is readable, will return true if it is (is true because its in read mode, if in write mode would not accept
print(my_list.readable())
'''
#this will read entire file, it will set cursor at the end of the file so we cannot use .readline or .readlines()[1] functions with it uncommented

print(my_list.read())
'''
#this will read one line and then move the cursor to the beginning of the next line
print(my_list.readlines()[1])
#remember to close the file too
my_list.close()


