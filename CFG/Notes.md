# Python Cheatsheet

Method: repeatable piece of code that completes
        a task for a specific data type

        - tied to specific data types
          - .upper()
          - .lower()
          - .title()
                eg:
                print("hello world".title())

### String
'''
multi line strings
allows us to write
multiple line string
'''
#### String Formatting

Example:
```
name = "Alice"
age = 30
message = f"My name is {name} and I am {age} years old"
print (message)

#f string

name = "Alice"
age = 30
message = "My name is {} and I am {} years old".format(name, age)
print(message)

#.format()

```

### Variable

Declare
Assign

### List

Indexed Lists

```
list_name[index]

# to replace a item:
fruits = ["Apple", "Plum", "Cherry"]    fruits[0] = "Banana"

#Output:
["Banana", "Plum", "Cherry"]

#Adding Items to List
fruits.extend(["Orange", "Grape", "Kiwi"])

#Remiving Item from List
fruits.pop()
#Do not need to state the value
```

#### Adding & Removing
```
# Adding
my_list.append(4) #adds 4 to the end of list
my_list.insert(1, 'a') #adds an 'a' to the list at index 1
my_list.extend([4,5]) #extends the list by adding [4,5] to the end

# Removing
my_list.remove(4) #removes the first occurence of the number 4 from the list
my_list.pop() #removes the last item from the list
my_list.clear() #removes all item from the list

# List Slicing
my_list[ start : stop : step ]
```

### Common Modules

```
import math # includes lots of math functions
from math import sqrt # import only the sqrt from the math module
import datetime # lots of helper functions with date and time
import timeit # can time program code
```

```
%a # returns the first three characters of the weekday, e.g. Wed
%A # returns the full name of the weekday, e.g. Wednesday
%B # returns the full name of the month, e.g. September
%w # returns the weekday as a number, from 0 to 6, with Sunday being 0
%Z # returns the month as a number, from 01 to 12
%Y # returns the year in four digit format
```

example:
```
import datetime

current_date = datetime.datetime.now()
print(current_date.strftime('%Y %b %d'))

new_date = datetime.date(2023,12,31)
print(new_date)

print(new_date.strftime('%a %B %Y'))
```

end of module:
```
# 1. Ask a user to input now many songs they would like to add to their playlist

playlist_length = int(input("How many songs would you like to add to your playlist? "))

# 2. store this information in a variable called: playlist_length

# 3. Using a for loop, prompt the user the enter the duration of each song in their playlist

song_durations = []
for i in range(playlist_length):
    duration = input(f"Enter the duration of song {i + 1} (in minutes): ")
    song_durations.append(duration)

# 4. Store the duration of each song in a list called: song_durations, and print these to the console.

print(song_durations)
```

### Dictionary
Adding and removing elements

- Adding
```
my_dict["email"] = "alice@gmail.com"
my_dict.update({"a":1})
```

- Removing
```
del my_dict["age"]
my_dict.pop("age")
my_dict.clear()
```

- retrieve info
```
keys()
values()
get("name")
get("name", "Not Found")
```

#### Convert Dictionaries to JSON
```
import json

person = {
  "name": "Xavier",
  "age": 23,
  "city": "Lin kong"
}
print(person)

json_person = json.dumps(person)
print(json_person)
```

### Pip and requests
```
# in terminal
% pip install requests

# then in script
import requests
```

### API (Application Programming Interface)
a set of rules that allows for different software to communicate with each other (request and exchange information)

to interact:
- send a request to API
- API processes request and send back response (usually ISON format)


1. client make a request to the server using HTTP methods
  (GET, POST, DELETE, PUT)
2. server processes the request
3. server responds with the data in JSON format
  (result_id:123, results:49328, query:"JSON")

#### HTTP methods
actions that define the type of operation that can be performed on the server

1. GET: retrieve data from the server
2. POST: send data to the server
3. PUT: update existing data on the server
4. DELETE: remove data from server
5. PATCH: apply partial updates on data on the server

**HTTP status**: responses from server, indicating outcome of the request

**code categories:**
1XX: Infromational
2XX: Success
3XX: Redirection
4XX: Client errer
5XX: Server error

### Assertion

a way of checing for conditions that should logically be 'true' in program

as a quick check to make sure input is as expected

if assertion is true, program continues to execute. If false, program raises an AssertionError and stops

make it quicker to find out what is wrong in the program


## Recap

- string: a sequence of characters enclosed in single or double quotation marks.
        uppercase: my.string.upper()
        lowercase: my_string.lower()

- get information from user:
        - getting input: input("Enter your name:")
        - storing input: name = input("Enter your name:")
        - converting input: int(input("Enter your age: ")
- numerica data
        integer, float

  - arithmetic operators:
    +  -  *  /  // %
- Variables: reusable labels used to store data
- String formatting: place a variable inside a message
  name = "Charlotte"
  f"Hello {name}, how are you?"
- Lists: store an ordered collection of items:
  students = ["Charlotte", "Adam", "Olivia"]
  - Indexing: students[0]
  - Slicing: students[1:2]
  - Removing: students.pop()
  - Adding: students.append("Tom")

- Boolean: either True or False
  - Comparison operators" compare 2 values and return a Boolean"
    ==  !=  <  >  <=  >=
  - Logical operators connect two or more conditions and return a Boolean: and or not

- If ... else statements - perform different actions depending on the condition we set
    if response == "Yes":
            print("You selected yes")
    if
    elif
    elif
    else

- For loop: repeat a block of code a set number of times:
  for i in iterable:
          print(i)
- while loop: repeat a block of code until a condition is no longer met:
  while i < 10:
          print(i)
          i += 1 # i = i + 1

- function: reusable block of code that is used to perform a specific task
          def my_function(arg1, arg2):
                  return arg1 + arg2
        - provide default argument to the function

- Dictionaries: store data as a key-value pair, unordered collection of items
  update: dictionary["name1"] = 10
  access: dictionary["name1"]
  extend: dictionary["new_name"] = 5
  delete: del dictionary["name1"]

  keys: dictionary.keys()
  values: dictionary.values()



