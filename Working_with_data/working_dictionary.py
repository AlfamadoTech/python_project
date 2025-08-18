# Syntax
# dictionary_name = {key1: value, key2: values}

# Creating Dictionaries
student = {
    "name": "Ada",
    "age": 20,
    "course": "Computer Science"
}
print(student)

# Using the dict() constructor
student_info = dict(name="John", age = 25, course = "Maths")
print(student_info)

# Empty dictionary
empty_dict = {}
print(empty_dict)

# Dictionary Comprehension
# Syntax {key_expression: value_expression for item in iterable if condition}

# Create a dictionary of numbers and their squares
squares = {x: x**2 for x in range(1,6)}
print(squares)

# with condition
even_cube = {x: x**3 for x in range(1, 10) if x % 2 == 0}
print(even_cube)

# From existing Dictionary
students = {"Ada": 85, "John": 40, "Musa": 65}

# Filter students who passed (score >= 50)
passed_students = {name: score for name, score in students.items() if score >= 50}
print(passed_students)

# Using String Keys
names = ["Ada", "John", "Musa"]
lengths = {name: len(name) for name in names}
print(lengths)

# Define a dictionary items

# Define a dictionary
student = {"name": "Ada", "age": 20, "course": "Computer Science"}

# Using Key
print(student["name"])

# Using get() method (avoids error if key is missing)
print(student.get("age"))
print(student.get("grade", "Not Found"))

# Modifying Dictionaries
student["age"] = 21 # Change value
student["grade"] = "A" # Add new key-value pair
student["matric"] = "FGN/100"
print(student)

# Removing items from dictionaries

# Using pop()
student.pop("grade")

# Using popitem() - removes last inserted key-value
student.popitem()

# Using del keyword
del student["course"]

# Using clear() - remove a;ll items
student.clear()

print(student)

# Dictionary Methods, .keys(), .values(), .update()

person = {"name": "Emeka", "age": 30}

# key()
print(person.keys())

# values()
print(person.values())

# items()
print(person.items())

# Update()
person.update({"age": 31, "city": "Lagos"})
print(person)

students = {
    "student1": {"name": "Ada", "age": 20},
    "student2": {"name": "John", "age": 22}
}
print(students["student1"]["name"]) #Access nested data

# Looping Through Dictionaries

# Define a dictionary
student = {"name": "Ada", "age": 20, "course": "Computer Science"}

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key_values
for key, value in student.items():
    print(f"{key}: {value}")

# Storing a student's biodata
student = {
    "name": "Chinedu",
    "age": 19,
    "department": "Engineering",
    "subjects": ["Maths", "Physics", "Chemistry"],
    "is_full_time": True
}

print(f"Name: {student['name']}")
print(f"subjects: {', '.join(student['subjects'])}")

# Create an empty dictionary
student = {}

# Add key-value pairs
student["name"] = "Goodness"
student["Interest"] = "AI"
student["Track"] = "AI_Dev"

print(student)

# List of dictionaries - Each student has their own dictionary
students = [
    {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
    {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
    {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
]

print(students[0]["Name"])
print(students[1]["Track"])
print(students[2]["Interest"])

# Dictionary of dictionaries - Each student is keyed by their ID
students = {
    "AI001" : {"Name": "John", "Interest": "AI", "Track": "AI_Eng"},
    "AI002" : {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
    "AI003" : {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
}

print(students["AI001"]["Name"])
print(students["AI002"]["Interest"])
print(students["AI003"]["Track"])

# Dictionary of lists - Each subject stores a list of scores
scores = {
    "Python": [85, 78, 92],
    "Pandas": [88, 74, 90],
    "Scikit-learn": [80, 95,87]
}

print(scores["Python"])
print(scores["Pandas"][1])
print(scores["Scikit-learn"][2])
