'''
# # print("hello, world!")
# # print(" 1 + 2 = ", 1 + 2)
# # print("1 + 2 = ", str(1 + 2))

# # ctrl + / - comment

# # lottoNums = [10, 16, 23, 32, 45]
# # print(lottoNums[0])

# # # Task 2
# # # Print the message "welcome to UCIL22212" out in your terminal
# # print("welcome to UCIL22212")
# # # Calculate what 2 * 3 is and print this out in your terminal with a suitable message using string concatenation
# # print("2 * 3 = ", str(2 * 3))
# # # Create a variable called name and print this in the terminal so it reads: "Hello {name}, Welcome to UCIL22212!"
# # name = "Tina"
# # print("Hello, " + name + ", Welcome to UCIL22212!")
# # # Create a variable called number and assign it the value 23.627. Print this number and its type to the terminal.
# # number = 23.627
# # print(number, type(number))
# # # Create two variables a & b. Set a to be 10 and b to be 5. Using print statements display the results for addition, subtraction, multiplication and division of the two variables.
# # a = 10
# # b = 5
# # print(a + b)
# # print(a - b)
# # print(a * b)
# # print(a / b)
# # # Create a list which contains the following:
# # # "welcome"
# # # 827
# # # "apples"
# # # 12.3
# # list = ["welcome", 827, "apples", 12.3]
# # # Print the 2nd element in our list and its type in the terminal.
# # print(list[1])
# # # Write a print statement which uses our list and prints the following: welcome apples, I have 827 of them.
# # print(list[0], list[2], ", I have", list[1], " of them.")
# # # Display the same message as Task 08 but use an f-string instead.
# # print(f"{list[0]} {list[2]}, I have {list[1]} of them.")
# # # Display the same calculations from Task 05 but use an f-string instead.
# # print(f"{a} + {b}")
# # print(f"{a} - {b}")
# # print(f"{a} * {b}")
# # print(f"{a} / {b}")
# # print(f"{a} + {b} = {a+b} \na - b = {a-b} \na * b = {a*b} \na / b = {a/b}")

# # # format is the most useful cos its easy to check spacings in the code
# # # print(f"Hi {name}, it's very nice to see you {age}")
# # # print(name + str(age))

# #Task 3
# name = "Sam"
# age = 32
# city = "Manchester"
# print(f"My friend {name} is {age} years old.")
# print(f"{name} lives in {city}.")

# a, b = 8, 3
# #我有点惊讶这个可以run
# sum_ab = a + b
# product_ab = a * b
# print(f"The sum of {a} and {b} is {sum_ab}.")
# print(f"Their product is {product_ab}.")

# name = "Eve"
# score = 95
# message = f"""
# Hello {name},
# Your lastest test score is {score:.2f}
# Keep up the great work!
# """
# print(message)

# price = 49.99
# discount  = 10
# message = f"""
# original price: ${price}
# Discount: {discount}%
# Final price: ${price - discount / 100:.2f}
# """
# print(message.upper())

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# message = f"""
# Hello {name.capitalize()}!
# Next year, you will be {age + 1} years old.
# Have a great day!
# """
# print(message.strip())

# x = 4
# y = 7

# if x >= 0 and x <= 10:
#     print("x is between 0 and 10")

# if y == 7 or y == 4:
#     print("y is either 7 or 4")

# FruitList = [
#     "apple",
#     "banana",
#     "cherry",
#     "date",
#     "elderberry",
#     "strawberry"
# ]

# # fruit in here can be replaced by any name
# # it's just a variable name to represent each element in the list as we loop through it
# # for fruit in FruitList:
# #     print(fruit)

# for fruit in FruitList:
#     if fruit == "strawberry":
#         print("We have strawberries!")

# for counter in range(0,len(FruitList)):
#     if FruitList[counter] == "strawberry":
#         print('strawberries are at position', counter)

# counter = 0
# while counter < len(FruitList):
#     print(FruitList[counter])
#     counter += 1

# Ctrl + C - end the terminal session
# while True:
#     print("This will run forever!")



### -------------------------------- Workshop 2 ---------------------------------- ###

# Create a conditional if-else statement that checks if a 
# variable called number is positive or negative print an 
# appropriate message.

# number = -7.5

# if number > 0:
#     print("This is a positive number!")
# elif number < 0:
#     print("This is a negative number!")
# else:
#     print("This number is zero!")

# Add an elif to the code in task 1. that checks if the 
# number is equal to 0 and print an appropriate message.

# Create a variable called course_name = "UCIL22212". 
# Using a for statement, print the characters individually 
# in each line.

# # 1
# course_name = "UCIL22212"
# for c in course_name:
#     print(c)

# # 2
# for i in range(len(course_name)):
#     print(f'number{i}: {course_name[i]}')

# # 3
# counter = 0
# while counter < len(course_name):
#     print(course_name[counter])
#     counter = counter + 1

# FruitList = ["Apple", "Orange", "whatever"]
# for x in FruitList:
#     print(x)

# Given the list days = ["mOnDay", "TueSDAY", "Wednesday", 
# "thursday", "FridaY"], print all the elements in lowercase
#  using a for-loop. Use .lower() on your strings to 
# achieve that.

# days = ["mOnDay", "TueSDAY", "Wednesday", "thursday", "FridaY"]
# for items in days:
#     print(items.lower())

# Given the following list element_list = ["Car", "Museum",
#  15, "Knight", 20, 30], only print the elements of type 
# integer from the list

# element_list = ["Car", "Museum", 15, "Knight", 20, 30]
# for items in element_list:
#     if type(items) == str:
#         print(items)

#Using a for statement with for i in range(), print all the
#  even numbers between 1 and 20 

for i in range(1, 20):
    if i%2 == 0:
        print(i)

# Using a while statement, iterate over the list in task 5 
# until the element 20 is found and then end the loop.

'''
'''
# ---------------------- Workshop 3 ------------------------

zoo = {
    "Lion": {"habitat": "Savannah", "diet": "Carnivore", "lifespan": 14},
    "Elephant": {"habitat": "Forest", "diet": "Herbivore", "lifespan": 60}
}

for animal in zoo:
    print(animal)

23


'''

'''
# ---------------------- Workshop 4 ------------------------

# Course Content

def print_name():
    print("Hello, I am David.")

print_name()


fruit1 = "Banana"
fruit2 = "Kiwi"
fruit3 = "Peach"

def print_yummy_fruit(fruit):
    print(f"I have a {fruit} and it's yum")

print_yummy_fruit(fruit1)
print_yummy_fruit(fruit2)
print_yummy_fruit(fruit3)


def print_name_message(name, surname):
    print(f"Hello I am {name} {surname}")

print_name_message("David", "Petrescu")


def print_name_message_default(name="Alan", surname="Turing"):
    print(f"Hello I am {name} {surname}")

print_name_message_default()


def add_numbers(a, b):
    return a + b

result = add_numbers(5, 5)
print(result)
print(add_numbers(5, 5))


def add_more_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add_more_numbers(5, 2, 1249, 214823))


def print_people(**people):
    for name in people:
        print(name, people[name])

print_people(name1="David", name2="Gareth", name3="Hamila")


class Food:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

    def is_high_protein(self):
        total_macros = self.protein + self.carbs + self.fat
        return (self.protein / total_macros) > 0.30

    def calorie_breakdown(self):
        protein_cals = self.protein * 4
        carb_cals = self.carbs * 4
        fat_cals = self.fat * 9
        print(f"\n{self.name} - Calorie Breakdown ({self.calories} kcal total):")
        print(f"  Protein : {protein_cals} kcal  ({self.protein}g)")
        print(f"  Carbs   : {carb_cals} kcal  ({self.carbs}g)")
        print(f"  Fat     : {fat_cals} kcal  ({self.fat}g)")

    def print_summary(self):
        label = "High protein" if self.is_high_protein() else "Not high protein"
        print(f"{self.name}: {self.calories} kcal | {label}")


class CruciferousVegetable(Food):
    def __init__(self, name, calories, protein, carbs, fat, florets):
        super().__init__(name, calories, protein, carbs, fat)
        self.florets = florets

    def get_florets(self):
        return self.florets


food1 = Food("Chicken Breast", calories=165, protein=31,  carbs=0,   fat=3.6)
food2 = Food("Banana",         calories=89,  protein=1.1, carbs=23,  fat=0.3)
food3 = Food("Peanut Butter",  calories=588, protein=25,  carbs=20,  fat=50)
food4 = Food("Greek Yoghurt",  calories=59,  protein=10,  carbs=3.6, fat=0.4)

food_list = [food1, food2, food3, food4]

for food in food_list:
    food.print_summary()

food1.calorie_breakdown()

broccoli = CruciferousVegetable("Broccoli", calories=35, protein=2.4, carbs=7, fat=0.4, florets=12)
broccoli.print_summary()
broccoli.calorie_breakdown()
print(broccoli.get_florets())

# ----------------------------- #

example_name = "savud Wharert"

print(example_name.capitalize())

def print_name(name = "Tina", surname = "Turing") -> None: # what it will return
    print("Hello, my name is", name, surname + "!")

print_name("Tina", "Shen")

def addNumbers(a,b) -> int: # Generally use as a guide, is not mandatory if it does not follow. Good for testing
    return a + b

sumNo = print_name()
    print(sumNo)

def addAllNumbers(*numbers): # provide list
    total = 0
    for number in numbers:
        total += number
    return total # return is important

print(addAllNumbers(5,6,2,1254,24,3,4242))

def print_people(**people): # supplying -> as key and value / provide dictionary
    for name in people:
        print(name, people[name])

print_people(name1 = "David", name2 = "Gareth", name3="Darcy")


name.capitalize()

'''
'''
# object oriented language - python
# everything is defined with classes - strings, numbers


# create your own class:
class Food:
    # initiating the class - constructor
    # dietrary tracker app context
    def __init__(self, name, calories, protein, carbs, fats):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carb = carbs
        self.fats = fats
    def calculateCalories(self):
        return self.protein * 4 + self.carb * 4 + self.fats * 9
    
banana = Food("Banana", 89, 1.1, 23, 0.3)

print(banana.calculateCalories())

'''

# Task 2:

# 1. A function that takes in two parameters and returns the square 
# of both values in a touple

def square_value(num1, num2):
    num1 = num1*2
    num2 = num2*2
    tuple = (num1, num2)
    return tuple

print(square_value(2,4))

# why have to put print() 而不是可以直接用square_value(2, 4)

# 2. A function with the following return statement. The default value 
# for the variable greeting should be "Greetings" and the function 
# should only contain one return statement (provided below).



def Greeting (name, greeting = "Greetings"):
    return f"{greeting}, {name}!"

print(Greeting("Tina"))
print(Greeting("Tina", "Hi"))