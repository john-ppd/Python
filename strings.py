python_strings = "this is a string"
my_bool = False #must be capital F and T for True
print("a word here, a new line \n also quotation marks\" " + python_strings)
#the \ tells python that the next thing after \ take literally so we can display " this way
print(my_bool)
#appening text
phrase1 = "hi "
phrase2 = "there"
print(phrase1 + phrase2)#this appends phrase 2 onto phrase 1

#make to text to upper and lower case
print("This is to upper " + phrase1.upper())
print("This is to lower " + phrase1.lower())

#check if phrase is upper or lower case completely
print(phrase1.isupper())
#can set to upper and then check, will happen in order
print(phrase1.upper().isupper())

#CHECK LENGTH
print(len(phrase1)) #returns three becase is "hi " is three characters

#Get specific character within the string
newVar = "Lets get a character from this string"
print(newVar[3]) #this will return the s because its the 4th location in the array

#.index("a_word") index is used to return the array index location of a character or string (where the first character is in a string)
newVar = "test string"
print(newVar.index("ing")) #locates where "ing" starst in the char array (location of i)

#REPLACING WORDS, .replace("replace this word", "with this word").
newVar = "hi"
print(newVar.replace("hi", "b  y  e") )
print("tester")

#PRINT String and Numbers same line
numbers = 123
string = "hi there"
print(str(numbers) + string)
