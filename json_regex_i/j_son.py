# JSON in Python


#Parse JSON - Convert from JSON to Python


# import json

# # some JSON: ---> comment
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x: ---> comment
# y = json.loads(x)

# # the result is a Python dictionary: ---> comment
# print(y["age"])



# Convert from Python to JSON:(use json.dumps())


# import json
    
#      # a python object (dict):
# x = {
# 	"name": "John",
# 	"age": 30,
# 	"city": "New York"
# }
#      # convet into JSON:
# y = json.dumps(x)
#      # The result is a json string:
# print(y)



# Convert python objects into JSON strings, and print the values:


# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("Apple", "Bananas")))
# print(json.dumps("Hello"))
# print(json.dumps(42))
# print(json.dumps(42.5))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))




# Convert a Python object containing all the legal data types:



# import json

# x = {
# 	"name": "John",
# 	"age": 30,
# 	"married": True,
# 	"divorced": False,
# 	"children": ("Ann", "Billy"),
# 	"pets": None,
# 	"cars": [
# 		{"model": "BMW", "mpg": 27.5},
# 		{"mode": "Ford Edge", "mpg": 24.1}
# 	  ]
# 	}
# print(json.dumps(x))




# Format the Result
# Use the indent parameter to define the numbers of indents:



# import json

# x = {
# 	"name": "John",
# 	"age": 30,
# 	"married": True,
# 	"divorced": False,
# 	"children": ("Ann", "Billy"),
# 	"pets": None,
# 	"cars": [
# 		{"model": "BMW", "mpg": 27.5},
# 		{"mode": "Ford Edge", "mpg": 24.1}
# 	  ]
# 	}

# 	# use four indents to make it easier to read the result:
# print(json.dumps(x, indent=4))




# Use the separators parameter to change the default separator:



import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))