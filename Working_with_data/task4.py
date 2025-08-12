'''
# 1. favourite life quote
favourite_quote = input("What is your favourite quote: ")
title_convert = favourite_quote.title()
print(favourite_quote)

# 2. Shopping list manager
shopping = []
shopping_list = input("Enter your shopping list: ")
shopping.append(shopping_list)
print(shopping)

# 3. Word Counter
sentence = input("Enter a sentence: ")
split_sentence = sentence.split(" ")
print(split_sentence)
print(len(split_sentence))
'''
# 4. Name Organizer
user_names = input("what are their name: ")
# convertering = "\n".join(user_names.lower().split())
converting = user_names.lower()
sort_list = (converting.split(" "))
print(sort_list.sort())




