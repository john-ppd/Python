#we are going to make a key and value pair, the way this works is that you define a word and it has a phrase associated with it, kind of like a word in the dictionary has a definition associated with it.

#all keys must be unique, jan is key, january is value
#doesn't have to be a string can be numbers too
month_conversions = {
   "Jan": "January",
    "Feb": "February",
    "Mar": "March to long for you to type?"
}
#You access the value using the key this way
print(month_conversions["Mar"])
#.get is better to use because we can pass a default value if there is a typo or incorrect entry
print(month_conversions.get("Mar", "DNE"))
print(month_conversions.get("ear", "DNE"))