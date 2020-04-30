#While loops
i = 1
while i <= 10:
    print(i)
    i+=1

secret_word = "bitcoin"
guess = "bitcoin"

while guess!=secret_word:
    guess = input("guess the secret word")
    if guess == secret_word:
        print("got it!!! breaking out of the loop")

#For loops, can use any veriable, in this case it will print one array[i] at a time
for i in "This String":
    print(i)

#ARRAY forloop, this will print each array element on a new line
names = ["john", "bob", "sev"]
for i in names:
    print(i)

#upto a NUMBER, will print 0 - 9
for i in range(10):
    print(i)

#print a RANGE, this will print 3 and 4
for i in range (3,5):
    print(i)

#print each ARRAY element
myarray = [1,2,3,4,5,6,7]
for i in range(len(myarray)):
    print(myarray[i])


