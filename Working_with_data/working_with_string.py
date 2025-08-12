"""
# Single quotes
name = 'Ada'

# Double quotes
greeting = "Hello"

# Triple quotes (for multi-line strings)
story = '''Once upon a time,
there was a coder named Ada.'''

# String with numbers and symbols
password = "p@ssw0rd123"

# Indexing
word = "Python"
print(word[0])  # P
print(word[-1])  # n

# Slicing
word = "Python"
print(word[0:4])   # Pyth
print(word[2:])    #thon
print(word[:3])    #Pyt
print(word[::2])   #Pto
print(word[::-1])

# String Concatenation & Repetition

# Concatenation
a = "Hello"
b = "World"
print(a + " " + b)   #Hello World

# Repetition
word = "Hi! "
print(word * 3)  #Hi! #Hi! #Hi!

# String Searching & Checking

# Membership
text = "Python programming"
print("Python" in text)    #True
print("Java" not in text)  #True

# find() / rfind()
text = "Hello Word"
print(text.find("o"))   # 4
print(text.rfind("o"))  # 7

# index() / rindex()
text = "Hello World"
print(text.index("World"))  # 6

# startswidth() / endswidth()
filename = "data.csv"
print(filename.startswith("data"))   # True
print(filename.endswith(".csv"))     # True
"""

sentence = "My name is Abdulmalik Adedotun and I'm Currently in AI Engineering training organized by Tijani Bosun Foundation and Ogun State ministry of Information and Communication"
print(sentence[:178])
print(sentence[1:20:5])
print(sentence.rfind("C"))
print(sentence.find("C"))
print(sentence.startswith("My"))
print(sentence.endswith("training"))
print("Abdulmalik" in sentence)
print("java" in sentence)
print("Python" not in sentence)
print(sentence)