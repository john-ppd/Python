'''
These are more comment types
should probably use # on each line tho
'''
def translate(phrase):
    translation = ""
    for i in phrase:
      print(i)
      #in checks to see if the value i is within the string, in this case the value i is one of characters from the string and checks to see if that charcter is a vowel, uses for loops and if statements are slightly different. The loop loops throgh the range. and the if statement will check the entire comparasin of the string to the current character before moving on.

      #i.lower() makes the string inputted go to all lower values and now we only need to check them and no cap values.
      if i.lower() in "aeiou":
          translation = translation + "g"
      else:
          translation = translation + i
    return translation

print(translate(input("enter a phrase")))
