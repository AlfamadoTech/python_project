# using parenthesis()
fruits = ("apple", "banana", "cherry")
print(fruits)

# without parenthesis
numbers = 1, 2, 3
print(numbers)

# single-item tuple
single_item = ("apple",)
print(single_item)
print(type(single_item))

# using tuple constructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

# ordered
colors = ("red", "green", "blue")
print(colors[0])

# Immutable
 #colors[1] = "yellow"
 # print(colors)

# Allow duplicates
numbers = (1, 2, 2, 3)
print(numbers)

# Mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)

# Nested tuple
nested = (("a", "b"), (1, 2))
print(nested)

# Tuple Operations

# Indexing
fruits = ("apple", "banana", "cherry")
print(fruits[1])
print(fruits[-1])

# Slicing
print(fruits[0:2])
print(fruits[::-1])

# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)

# Repetition
nums = (1, 2)
print(nums * 3)

# Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)
print("grape" not in fruits)

# Iteration
for fruit in fruits:
    print(fruits)

# unpacking tuple
numbers = (1, 2, 2, 3, 4)
print(numbers.count(2))
print(numbers.index(3))

# Tuple to list
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst)

# list back to tuple
t = tuple(lst)

# Built in Function with tuples
nums = (4, 1, 7, 3)

print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))