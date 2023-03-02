# RegEx in Python


# Search the string to see if it starts with "The" and ends with "Spain":


# import re
# txt = "The rain in Spain"

# x = re.search("^The.*Spain$", txt)
# if x:
# 	print("YES! the match found.")
# else:
# 	print("No match")




# Metacharacters
# Metacharacters are characters with a special meaning:



# [] --> set of characters

# import re
# txt = "The rain in Spain"
# """ Find all lower case characters alphabetically 
#     between a and m """
# x = re.findall("[a-m]", txt)
# print(x)



# "\"    Signals a special sequence    "\d"


# import re
# txt = "That will be 59 dollars"

#       # Find all digit charecters
# x = re.findall("\d", txt)
# print(x)



# "." Any character (except newline character)    "he..o"


# import re
# txt = "hello planet"
"""Search for a sequence that starts 
	 with "he", followed by two (any) 
	 characters, and an "o":"""
# x = re.findall("he..o", txt)
# print(x)



# "^" Starts with    "^hello"


# import re
# txt = "hello planet"
#    # check if the string starts with hello
# x = re.findall("^hello", txt)
# if x:
# 	print("The string starts with 'hello' ")
# else:
# 	print("No match")



# $ Ends with     "planets$"


# import re
# txt = "Hello planet"
#    # Check if the string ends with planet
# x = re.findall("planet$", txt)
# if x:
# 	print("YES! the string ends with 'planet'")
# else:
# 	print("No match")




# "*"  Zero or more occurances     "he.*o"



# import re
# txt = "hello planet"
# """Search for a sequence that starts with 'he' followed 
# by 0 or more characters, and an 'o' """
# x = re.findall("he.*o", txt)
# print(x)



# "+" One or more occurances   "he.+"


# import re
# txt = "hello planet"
#     #Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
# x = re.findall("he.+o", txt)
# print(x)



# "?"  Zero or one occurances   "he.?o"



# import re
# txt = "hello planet"
# 	#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
# x = re.findall("he.?o", txt)
# print(x)
# 	#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"



# {}   Exactly the specified number of occurances    "he.{2}o"



# import re
# txt = "hello planet"
# 	#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
# x = re.findall("he.{2}o", txt)
# print(x)



# |  Either or   "falls/stays"


# import re
# txt = "The rain in Spain falls in the plain!"
# 	#Check if the string contains either "falls" or "stays":
# x = re.findall("falls|stays", txt)
# if x:
# 	print("Yes! there is a match")
# else:
# 	print("No match")



# The findall() Function
# Te find all function returns the list of all matches


# import re
# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)



# The search() Function

# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:




# Search for the first white-space character in the string:
# import re

# txt = "The rain in Spain"
# x = re.search("\s", txt)
# print("The first white-space character is located in position: ",
# 	x.start())



# If no matches are found, the value None is returned


# import re
# txt = "The rain in Spain"
# x = re.search("Portugal", txt)
# print(x)



# The split() Function 
# The split() function returns a list where the string has been split at each match:



# Split at each white-space character:
# import re
# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)




# Split the string only at the first occurrence:
# import re
# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)



# The sub() Function
# The sub() function replaces the matches with the text of your choice: 




# Replace every white-space character with the number 9:
# import re
# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt,)
# print(x)



# Replace the first two occurances
# import re
# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)




# Match Object
#the match object has the methods and the properties used to retrieve information about the search and the result: 



# .span()   ---> returns a tuple contaning the start-, and end positions of the match
# .string() ---> Returns the stringg passed into the function
# .group()  ---> Returns the part of the string where there was a match



#.span()



# import re 
# txt = "The rain in Spain"
# #Search for an upper case "S" character in the beginning of a word, and print its position:
# x = re.search(r"\bS\w+", txt)
# print(x.span())



# .string()



# Print the string passed to the function
# import re
# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.string)




# .group()



# Print the part of the string where there was a match
# import re
# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.group())


import pyautigui as pg
import time

print("print 10 times")
