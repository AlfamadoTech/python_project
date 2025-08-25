# Functions (first level of modularity)
# See Examples of use here
# range()
for i in range(3):
    print(i)   # 0, 1, 2

# zip()
names = ["Esther", "Preciou", "Kennie"]
scores = [85, 90, 75]
for n, s in zip(names, scores):
    print(n, "scored", s)

# map()
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)    # [1, 4, 9, 16]

# filter()
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)   # [2, 4]

# Student Performance & Feedback System
# Step 1: Input student data
name1 = input("Enter first student name: ")
score1 = int(input("Enter score for " + name1 + ": "))

name2 = input("Enter second student name: ")
score2 = int(input("Enter score for " + name2 + ": "))

name3 = input("Enter third student name: ")
score3 = int(input("Enter score for " + name3 + ": "))

# Step 2: Store in lists
names = [name1, name2, name3]
scores = [score1, score2, score3]

# Step 3: Display data
print("\nStudent Data:")
for index, (n, s) in enumerate(zip(names, scores)):
    print(f"{index + 1}. {n} - {s}")

# Step 4: Summary using built-ins
total = sum(scores)
average = round(total / len(scores), 2)
highest = max(scores)
lowest = min(scores)

print("\nPerformance Summary:")
print("Total Score:", total)
print("Average Score:", average)
print("Highest Score:", highest)
print("Lowest Score:", lowest)

# Step 5: Ranking (using scorted and zip)
ranked = sorted(zip(scores, names), reverse=True)
print("\nRanking:")
for rank, (score, name) in enumerate(ranked, 1):
    print(f"{rank}. {name} - {score}")

# Step 6: Check data types
print("\nData Type Checks:")
print("Type of names:", type(names))
print("Type of scores:", type(scores))
print("ID of names list:", id(names))
print("ID of scores list:", id(scores))

# Step 7: Filter passing students (>=50)
passing = list(filter(lambda s: s >= 50, scores))
print("\nPassing Scores:", passing)

# Step 8: Map names to uppercase
upper_names = list(map(lambda n: n.upper(), names))
print("Uppercase Names:", upper_names)

# Step 9: Use help() to show documentation of len
print("\nHelp on len():")
help(len)

# User Define Function
'''
syntax
def function_name(takes in input):
    process block
    output block
'''
# Defining a function
def greet():
    print("Hello, Welcome to AI Fellowship!")

# When you want to use a function, this is how to call it
# And you can call it as many times as possible.
greet()
greet()
greet()

# Function Arguments and Parameters
# Function with an argument - the placeholder
def greet(name):
    print("Hello", name, "Welcome to Python learning")

# Calling with parameter -  the actual name
greet("Class rep")
greet("Ridwan")

# When to Use return, print(), and yield keywords inside a function
# A. Print()
def greet(name):
    print("Hello", name)

# Function call
result = greet("Abdulmalik")

# You will notice that it did not store the name
print("Result", result)

# B. Return
def add(a, b):
    return a + b
# Function call
result = add(4, 6)
print("The sum is: ", result)

# C. Yield
def count_up_to(n):
    i = 1
    while i <= n:
        i += 1

# Using the generator
for number in count_up_to(5):
    print(number)

# More on Function Arguments(Types of Argument)
# 1. Positional Arguments
def introduce(name, track):
    print("My name is", name)
    print("I am learning", track,".")

# function call
introduce("Abdulmalik", "AI Engineering")  # Correct order

# Change the arrangement and watch the output
introduce("AI Engineering", "Abdulmalik") # Incorrect order, this will throw a semantic error

# 2. Keyword Arguments
def introduce(name, track):
    print("My name is", name)
    print("I am learning", track,".")

# function call
introduce(name = "Abdulmalik", track = "AI Engineering")

# Change the arrangement and watch the output
introduce(track = "AI Engineering", name = "Abdulmalik")

# Default Arguments
def introduce(name, track = "AI Engineeering"):
    print("My name is", name)
    print("I am learning", track,".")

# function call
# Without specifying the default argument, but watch the output
introduce("Khadijah")

# Specify the default argument and watch the output
introduce("Qowiyyah Ahmed", track = "AI Development")

# Varying Length Arguments
# A. non-keyword (tuple)
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum: ", total)

# function call
# Take note of the output
add_numbers(2, 4, 6)
add_numbers(10, 20, 30, 40, 50)

# B. keyword argument (dictionary)
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# function call - Take note of the output
student_details(name="Abdulmalik", track="AI Engineering", interest="FinTech")

# Lets implement on full code
# Define student profile function
# Ensure to not the order of arrangement of the types of arguments used.
# This is how to arrange it of you are using everything or some of the together
def participant_profile(name, age, track="AI Engineering", *skills, **extra_info):
    """
    Generate a profile for a bootcamp participant using different types of arguments.
    """
    profile = f"\n--- Bootcamp Participant Profile ---\n"
    profile += f"Name: {name}\n"
    profile += f"Age: {age}\n"
    profile += f"Track: {track}\n"

    # Skills (from *args)
    if skills:
        profile += "Skills: " + ", ".join(skills) + "\n"
    else:
        profile += "Skills: Not yet specified\n"

    # Extra info (from **kwargs)
    if extra_info:
        profile += "Additional Info:\n"
        for key, value in extra_info.items():
            profile += f" - {key.capitalize()}: {value}\n"
    return profile 

# Lets test
# Example 1: Using only positional arguments
print(participant_profile("Abdulmalik", 24))

# Example 2: Adding keyword/default argument
print(participant_profile("Ridwan", 29, track="AI Engineering"))

# EXample 3: Adding variable-length positional arguments (*args)
print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine Learning"))

# Example 4: Adding variable-length keyword arguments (**kwargs)
print(participant_profile(
    "Faidat", 22, "CyberSecurity", "Networking",
    "Ethical Hacking", "Python", "Data Structure",
    interest="Blockchain", city="Shagamu", phone="08123456789"
))

# Namespace and Scope
# Namespace
# Types of Namespaces
# 1. Built-in namescape - Provided by python (e.g., len, print, list).
# 2. Global namescape - Names defined at the top level of script or module
# 3. Local namespace - Names created inside a function

# Global namespace
employee = "General Employee"

def IT_department():
    # Local Namespace inside IT_department
    employee = "Chris (IT)"
    print("Inside IT Department:", employee)

def Training_department():
    # Local Namespace inside Training_department
    employee = "Chris (Training)"
    print("Inside Training Department:", employee)

print("In Global Namespace:", employee)  # Refers to global variable

IT_department()    # Uses local variable in IT
Training_department()    # Uses local variable in training

# using a built-in namespace function
print("Length of 'Python':", len("Python"))

# So 'Chris' can exist in more than one namespace without conflict.
# Please, take your time to study the output carefully.

# Scope - defines where in the code a name is accessible. Python follows the LEGB Rule(Order of search for a variable):
# L- Local -> inside the current function.
# E- Enclosing -> Inside any enclosing function
# G- Enclosing -> At the top level of the script/module
# B- Built-in -> Python built-in functions/objects

x = "global x"     # Global namespace

def outer():
    x = "enclosing x"   # Enclosing Namespace

    def inner():
        x = "local x"    # Local Namespace
        print("Inside inner:", x)   # Local wins

    inner()
    print("Inside outer:", x)   # Enclosing

outer()
print("In global:", x)

### Global keyword
# Used when you want to modify a global variable inside a function.
x = 5
def change_global():
    global x
    x = 10    # modifies the global x

change_global()
print(x)    # Output: 10

# non local keyword
# Used in nested functions when you want to modify the variable from the enclosing scope (not global).

def outer():
    x = "Outer x"

    def inner():
        nonlocal x
        x = "change by inner"
        print("Inside inner:", x)

    inner()
    print("Inside outer:", x)

outer()

# Lambda Function
# A lambda function is a small, anonymous function (no name) defined using lambda keyword.
# It can hav any number of arguments, but only one expression
# The result of the expression is automatically returned
# Syntax - lambda arguments: expression

# when to use lambda
# When you need a short, throwaway function(not reuseable).
# To avoid writing full def functions for small tasks.
# Used with functions like map(), filter(), sorted(), reduce().

# Normal function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

print(square(5))
print(square_lambda(5))
# Watch the output and note the difference

# This one has more that one arguments.
add = lambda a, b: a + b
print(add(3, 7))   # Output: 10

# Let us use lambda to apply the square function to a list
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)   # Output: [1, 4, 9, 16]

# Lets use lambda to filter even numbers
numbers = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # Output: [10, 20, 30]

# Lets use lambda to sort the tuple within a list.
students = [("Ayo", 20), ("Bola", 18), ("Chika", 22)]

# Sort by age
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)
# Output: [('Bola', 18), ('Ayo', 20), ('Chika', 22)]

students_sorted_descending = sorted(students, key=lambda student: student[1], reverse=True)
print(students_sorted_descending)
# Output: [('Ayo', 20), ('Chika', 22), ('Bola', 18)]

students_sorted_alphabetically = sorted(students, key=lambda student: student[0])
print(students_sorted_alphabetically)
# Output: [("Ayo", 20), ("Bola", 18), ("Chika", 22)]