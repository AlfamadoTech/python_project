fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print(fruits)

fruits = ["apple", "banana"]
trophical = ["mango", "pineapple"]
fruits.extend(trophical)
print(fruits)

fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)

fruits = ["apple", "banana", "cherry"]
last_fruits = fruits.pop()
print(last_fruits)
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

fruits = ["apple", "banana", "cherry"]
position = fruits.index("banana")
print(position)

fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.count("banana"))

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)

fruits = ["apple", "banana", "cherry"]
new_list = fruits.copy()
print(new_list)