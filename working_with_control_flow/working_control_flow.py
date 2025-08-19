# Control Flow in Python
# Conditional Statement

# if statement
age = 20
if age >= 18:
    print("You are eligible to vote")
# Some usecases
# Checking for eligibility
# Validating login attempts
# Ensuring a minimum purchase requirement, etc.

# if-else Statement
# Provides two alternative paths
wallet = 400
price = 500
if wallet >= price:
    print("Purchase successful")
else:
    print("Insufficient balance")
# Some usecases
# Deciding success or failure of a payment
# Granting or denying access to a system
# Determining pass/fail in an exam

# if-elif-else Statement
score = 85
if score >= 70:
    print("Grade A")
elif score >= 50:
    print("Grade B")
else:
    print("Grade C")
# Some usecases
# Student grading systems
# Assigning ticket categories (VIP, Regular, Student)
# Categorizing temperatures (Hot, Warm, Cold), etc.

# Nested if
age = 19
citizen = True

if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You must be a citizen to vote")
else:
    print("Too young to vote")
# Some usecases
# Voting eligibility (age + citizenship)
# Banking (account active + balance sufficient)
# school admission (age + grade level)

# Loops
# for loop
# Iterates through each element in a LIST
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")
# some usecases
# Iterating through shopping lists
# Checking availability of products
# Displayoing student names, e.t.c

# Iterate through each element in a TUPLE. This works like lists, but remember that tuples are immutable
coordinates = (0.34654, -0.48585, 0.57477)
for point in coordinates:
    print(f"Point: {point}")

# Iterates through each element in a DICTIONARY. Remember that dictionaries have key-value pairs.
student = {"name": "Tunde", "age": 16, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")
# some usecases
# Reading database records
# showing user profile details
# checking configuration settings, etc.

# Iterates through each element in a STRING. Remember that strings are sequence of characters
word = "PYTHON"
for char in word:
    print(char)
# some usecases
# counting vowels/consonants
# Password validation (checking digits/special chars)
# text analysis, etc.

# While loop
count = 1
while count <= 5:
    print("Number:", count)
    count += 1

# Incrementing with while
num = 1
while num <= 10:
    print(num, end=" ")
    num += 1

# Decrementing with while
timer = 10
while timer > 0:
    print("Countdown:", timer)
    timer -= 1

# while with user input
# keep asking until the user enters a correct password
password = ""
while password != "python123":
    password = input("Enter the password: ")
print("Access Granted!")

# Understanding while True
# Commonly used when
# You don't know in advance how many times you want the loop to run
# You want to keep asking the user for input a valid condition is met
# You are building continuous programs like menus, login systems, or simulations

# Keep asking the user for a name they type "exit"
while True:
    name = input("Enter your name(type 'exit' to quit): ")
    if name.lower() == "exit":
        print("Goodbye")
        break
    print(f"Hello, {name}")

# Loop Control Statements (break, continue and pass)
# break - Stops loop immediately. it is used if a condition is met and there's no need to continue looping.
for num in range(1, 10):
    if num == 5:
        break
    print(num)
# The loop stops completely when num == 5

# Continue - Skip the current iteration and moves to the next one. it is used if you want to ignore some values but keep the loop running
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
# 3 is skipped, but the loop continues
# Some usecases
# Skip invalid data
# Ignore unwanted characters (like spaces in a string)
# Continue running but avoid certain cases, etc.

# Pass - Does nothing. A placeholder to avoid errors. It is used if you haven't written the code yet but want to keep the structure
for num in range(1, 6):
    if num ==3:
        pass # do nothing for now
    else:
        print(num)
# At num == 3, Python executes pass (nothing happens)
## Some usecases
# Writing code structure (to fill in later)
# Placeholders in class/method definitions
# Temporarily disable parts of code

while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Goodbye")
    elif choice == '3':
        print("Exiting Program...")
        break
    else:
        print("Invalid choice. Try again.")

# Try and use while True for validation
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        print(f"Your age is {age}")
        break
    else:
        print("Invalid input. Please enter a number.")

# Let's make a guess
secret = "python"
while True:
    guess = input("Guess the secret word: ")
    if guess.lower() == secret:
        print("Correct! You guessed the word: ")
        break
    else:
        print("Wrong! Try again")

# Do you remember this?
balance = 1000
while True:
    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        print(f"Your balance is: {balance}")
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"withdraw sucessful. New balance: {balance}")
        else:
            print("Insufficient funds.")
    elif choice == "3":
        print("Thank you for using our ATM. Goodbye")
        break
    else:
        print("Invalid option. Try again")