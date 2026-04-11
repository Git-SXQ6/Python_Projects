"""
print("hello, world!")
print(" 1 + 2 = ", 1 + 2)
print("1 + 2 = ", str(1 + 2))

ctrl + / - comment

lottoNums = [10, 16, 23, 32, 45]
print(lottoNums[0])

# Task 2
# Print the message "welcome to UCIL22212" out in your terminal
print("welcome to UCIL22212")
# Calculate what 2 * 3 is and print this out in your terminal with a suitable message using string concatenation
print("2 * 3 = ", str(2 * 3))
# Create a variable called name and print this in the terminal so it reads: "Hello {name}, Welcome to UCIL22212!"
name = "Tina"
print("Hello, " + name + ", Welcome to UCIL22212!")
# Create a variable called number and assign it the value 23.627. Print this number and its type to the terminal.
number = 23.627
print(number, type(number))
# Create two variables a & b. Set a to be 10 and b to be 5. Using print statements display the results for addition, subtraction, multiplication and division of the two variables.
a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
# Create a list which contains the following:
# "welcome"
# 827
# "apples"
# 12.3
list = ["welcome", 827, "apples", 12.3]
# Print the 2nd element in our list and its type in the terminal.
print(list[1])
# Write a print statement which uses our list and prints the following: welcome apples, I have 827 of them.
print(list[0], list[2], ", I have", list[1], " of them.")
# Display the same message as Task 08 but use an f-string instead.
print(f"{list[0]} {list[2]}, I have {list[1]} of them.")
# Display the same calculations from Task 05 but use an f-string instead.
print(f"{a} + {b}")
print(f"{a} - {b}")
print(f"{a} * {b}")
print(f"{a} / {b}")
print(f"{a} + {b} = {a+b} \na - b = {a-b} \na * b = {a*b} \na / b = {a/b}")

# format is the most useful cos its easy to check spacings in the code
# print(f"Hi {name}, it's very nice to see you {age}")
# print(name + str(age))

#Task 3
name = "Sam"
age = 32
city = "Manchester"
print(f"My friend {name} is {age} years old.")
print(f"{name} lives in {city}.")

a, b = 8, 3
#我有点惊讶这个可以run
sum_ab = a + b
product_ab = a * b
print(f"The sum of {a} and {b} is {sum_ab}.")
print(f"Their product is {product_ab}.")

name = "Eve"
score = 95
message = f"""
# Hello {name},
# Your lastest test score is {score:.2f}
# Keep up the great work!
"""
print(message)

price = 49.99
discount  = 10
message = f"""
# original price: ${price}
# Discount: {discount}%
# Final price: ${price - discount / 100:.2f}
"""
print(message.upper())

name = input("Enter your name: ")
age = int(input("Enter your age: "))

message = f"
Hello {name.capitalize()}!
Next year, you will be {age + 1} years old.
Have a great day!
"
print(message.strip())


name = "tina"
age = 22
city = "Manchester"
activity = "went to Laufey's concert!"

print(f"Hi my name is {name}, I am {age} years old now and " 
      f"currently live in {city}, I want to share with you one " 
      f"of my happiest moment, that I just {activity}!")


print(2*3)

number = 2 * 3
print(f"2 * 3 equals to {number}")

print(f"hello {name}, welcome to UCIL2212")

number = 23.627
print(number, type(number))

# Create two variables a & b. 
# Set a to be 10 and b to be 5. 
# Using print statements display the results for addition, 
# subtraction, multiplication and division of the 
# two variables.
a, b = 10, 5
print(f"
      #   addition: a + b = {a + b}
      #   subtraction: a - b = {a - b}
      #   multiplication: a * b = {a * b}
      #   division: a / b = {a / b}
      ")

# Create a list which contains the following:
# "welcome"
# 827
# "apples"
# 12.3
content = ["welcome", 827, "apples", 12.3]

#Print the 2nd element in our list 
# and its type in the terminal.

print(content[1])

#Write a print statement which uses our list and 
# prints the following: welcome apples, I have 827 of them.

print("welcome", content[2] + ", I have", content[1], "of them.")

#Display the same message as Task 08 but use an f-string 
# instead.

print(f"welcome {content[2]}, I have {content[1]} of them.")

# Display the same calculations from Task 05
#  but use an f-string instead.

price = 49.99
discount = 10

message = f"
Original prince: ${price}
Discount: {discount}%
Final prince: ${price - discount / 100:.2f}
"

print(message.upper())



day = "Beautiful"
print("Today is " + day)

print("Hello")
"""
'''

# ————————————————————————————————————————————————————————————————————————#
##这题有问题！！带去dropin问一下！！！
name = input("Enter your name:")
age = int(input("Enter your age:"))

message = f"Hello{name.capitalize()}!\nNext year, you will be {age + 1} years old.\nHave a great day!"
print(message.strip())

# 

# 我如果存入了一次tempinCel的数值
# 后面我就会出现根本不问user数值直接出最后结果的情况

tempinCel = input("Give me the temperature (in degree Celsius): ")
tempinFah = (float(tempinCel) * 1.8) + 32
print("This temperature is", float(tempinFah), "in Fahrenheit.")



'''

'''

# Workshop 3

fruits = [

]

fruits_dict = {
    "Apple": 5, "Banana": 8, "Grapes": 3, 
    "Pineapple": 9, "Mango": 12, "Strawberry": 6
}

print(fruits_dict["Mango"])

fruit_to_check = "Banana"

if fruit_to_check in fruits_dict:
    print(f"We have {fruits_dict[fruit_to_check]} {fruit_to_check}s.")

'''

'''
# Nesting, nested?

adv_fruits = {
    "Apple": {
        "quantity": 5, 
        "colour": "green",
        "taste": "yummy"
    },
    "Banana": {
        "quantity": 8,
        "colour": "yellow",
        "taste": "super yummy"
    }
}

print(adv_fruits)

fruit_to_check = "Banana"
if fruit_to_check in adv_fruits:
    print(f"{adv_fruits[fruit_to_check]["taste"]}")

# File handling

file = open("fruits.txt", "r")  #"r" stands for read the file
contents = file.read()
print(contents)
file.close()  # it would take up some performance of the laptop but very minor

with open("fruits.txt", "r") as file:
    contents = file.read()
    print(contents)
    
    first_line = file.readline()
    # print("First line", first_line)
    print(lines)
    # print each line


with open("fruits.txt", "w") as file:
    file.write("MagicFruit")
# write - overwrite (only magic fruit in the file)

with open("fruits.txt", "a") as file: #append
    file.write("\nMagicFruit")


# create a backup file
with open("fruits.txt", "r") as original:
    original_content = original.read()
    with open ("fruit_backup.txt", "w") as backup:
        backup.write(original_content)

'''


# Workshop 3 practices
countries_dic = {
    "UK": 3, "India": 30, "China": 25,
    "USA": 20, "France": 5, "Spain": 6
}

print(countries_dic)

countries_dic["Iceland"] = 3
print(countries_dic)

max_value = 0
max_key = None
for key, value in countries_dic.items():
    if value > max_value:
        max_value = value
        max_key = key
print(f"The country with the largest population is {max_key}, and its population is {max_value}.")

del(countries_dic["France"])
print(countries_dic)


for name, population in countries_dic.items():
    print(f"{name}: {population}")

# Create a new dictionary which allows you to store the countries name, 
# population, capital city & continent

# countries_data = {
#     "China": {
#         "population": 14,
#         "capital city": "Beijing",
#         "continent": "Asia" 
#     },
#     "UK": {
#         "population": 3,
#         "capital city": "London",
#         "continent": "Europe"
#     },
#     "Switzerland":{
#         "population": 1,
#         "capital city": "Zurich",
#         "continent": "Europe"
#     }
# }

# value = 0


# # Print out all counties which are in Europe.
# # Print those with a population greater than the average population in the dictionary
