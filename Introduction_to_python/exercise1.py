"""
# String reverse
reverse = "Hello World"
print(reverse[::-1])

# Largest number
num = [10, 20, 5, 8, 50]
print(max(num))

# print number 1 to 50
print(*range(1, 51))

# sum of number
sum = [1, 2, 3, 4, 5]
print (sum[0]+sum[1]+sum[2]+sum[3]+sum[4])

# the length of a string entered by the user
word_length = "Welsome to python basics"
print(len(word_length))

# Simple Calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

add = num1 + num2
sub = num1 -num2
mult = num1 * num2
div = num1 / num2

print(f"sum of number: {add}")
print(f"subraction of number: {sub}")
print(f"multiplication of number: {mult}")
print(f"division of number: {div}")

# Calculate the area of a circle (hint: area = πr²)
radius = float(input("Enter radius of the circle: ")) 
pie = 22/7
area = pie * radius * radius
print(f"Area of circle is {area}")

#  Write a Python function that takes a list and returns a new list with only unique elements
fruits = ["Apple", "Mango", "Banana", "Golden Melon", "Paw Paw", "Pineapple", "Orange", "Mango", "Orange", "Banana", "Apple"]
print(set(fruits))

#  Find the smallest number in a list: [7, 2, 9, 4, 1]
smallest = [7, 2, 9, 4, 1]
print(min(smallest))

# Convert temperature from Celsius to Fahrenheit
temperature_in_celsius = float(input("Enter the temperature in celsius: "))
temperature_in_fahrenheit = (temperature_in_celsius * 1.8) + 32
print(f"Temparatue in fahrenheit is {temperature_in_fahrenheit} ")

# Swap two variables without using a third variable.
a = 10
b = 5
a, b = b, a

# Perimeter of a rectangle
length = float(input("Enter lenghth of a rectangle: "))
breadth = float(input("Enter the breadth of rectangle: "))
perimeter = (2*length) + (2*breadth)
Area = length * breadth
print(f"The perimeter of a rectangle is {perimeter} and area is {Area}")

# Create two string variables, `first_name` and `last_name`, with your first and last names. Concatenate them to form a full name and assign it to a new variable `full_name`. Print the `full_name` in uppercase.
first_name = "Abdulmalik"
last_name = "Adedotun"
full_name = first_name + " " + last_name
print(full_name.upper())
print(full_name.lower())

# You have a variable `num_of_books` storing the number of books you have read this month, but it's currently in the form of a string. Create a new variable `books_read` by casting `num_of_books` to an integer. Then calculate the average number of books read per week, assuming there are four weeks in a month.
num_of_books = "15"
books_read = int(num_of_books)
avg_book_per_week = books_read / 4
print(f"average book read in a week is {avg_book_per_week}")
"""
# Create a tuple named `tree_tuple` containing three elements: `8`, `'apple'`, and `'Granny Smith'`.
# Find the length of the tuple.
# Access the second element, `'apple'`, in the `tree_tuple` using an index and assign the value to a variable called `fruit`. Print the variable. 
# Attempt to change the value of `'apple'` in `tree_tuple` to `'pear'` using assignment.
# Create a new tuple called `text_only` and place the last two elements of `tree_tuple` into it.
# Create two tuples: `fruit_summer` and `fruit_winter`, with elements (`'peach'`, `'apricot'`, `'plum'`) and (`'lemon'`, `'orange'`, `'grapefruit'`), respectively. Print the tuples to screen in the same print statement.
# Combine these following two tuples, `fruit_summer` and `fruit_winter`, to form a new tuple, `all_fruit`. Print the new tuple to the screen.
# Confirm how many times the element `'peach'` appears in `all_fruit`.
# Suppose we have the `combined_info` tuple shown in the block of code below, containing three elements – the colour of the fruit, the age of the tree, and the type of tree. We'd however like to work with these elements individually and need to create variables (colour, age, tree_type) for each of the elements in the tuple. 
# combined_info = ('yellow', 5, 'lemon')

tree_tuple = (8, 'apple', 'Granny Smith')
print(len(tree_tuple))
print(tree_tuple[1])
print(tree_tuple.index('apple'))
tree_tuple[1] = 'pear'
# text_only = ('apple', 'Granny Smith')
text_only = tree_tuple[1:3]

fruit_summer = ('peach', 'apricot', 'plum')
fruit_winter = ('lemon', 'orange', 'grapefruit')
print(f"the fruit produced in the summer are {fruit_summer} and for summer are {fruit_winter}")
print(fruit_summer, fruit_winter)
all_fruit = (fruit_winter + fruit_summer)
print(all_fruit)
print(all_fruit.count('peach'))

