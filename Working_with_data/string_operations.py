# Upper
name = "Abdulmalik Adedotun"
print(name.upper())

# Lower
name = "Abdulmalik Adedotun"
print(name.lower())

# Title
sentence = "Python is dynamic"
print(sentence.title())

# strip
text = "    Abuja    "
print(text.strip())

# replace
message = "I love Java"
print(message.replace("Java", "Python"))

# swapcase
text = "Hello ABEOKUTA"
print(text.swapcase())

# rstrip
text = "Nigeria   "
print(text.rstrip())

# split
fruits = "mango orange banana"
print(fruits.split())

# rsplit
text = "one,two,three,four"
print(text.rsplit(",", 2))

text = "one,two,three,four"
print(text.rsplit(",", 2))

# splitlines
lines = "Line 1\nLine 2\Line 3"
print(lines.splitlines())

# join
words = ["I", "Love", "Python"]
print(" ".join(words))

# center
text = "Python"
print(text.center(20, "-"))

# ljust
text = "Python"
print(text.ljust(10, "*"))

# rjust
text = "Python"
print(text.rjust(10, "*"))

# zfill
num = "42"
print(num.zfill(5))

# isalpha
print("Lagos".isalpha())
print("Lagos123".isalpha())

# isdigit
print("12345".isdigit())
print("123a".isdigit())

# isalnum
print("Python3".isalnum())
print("Python 3".isalnum())