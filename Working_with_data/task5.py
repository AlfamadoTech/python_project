'''# 1. Create and display
dish = []
for i in range(3):
    favourite_dish = input(f"Enter your three favourite Nigeria food {i+1}: ")
    dish.append(favourite_dish)
dishes = tuple(dish)
print(dishes)
print("\n".join(dishes))

# 2. Tuple and Input
friends = [
            input("First friend: "),
            input("Second friend: "),
            input("Third friend: "),
            input("Fourth friend: "),
            input("Fifth friend: ")
]
print(tuple(friends))
best_friend = tuple(friends)
print(best_friend[::-1])

# 3. Tuple Operation
nigeria_state = tuple([
                        input("first nigeria state: "),
                        input("Second nigeria state: "),
                        input("Third nigeria state: "),
                        input("fourth nigeria state: "),
                        input("fifth nigeria state: ")
])
print(f"{nigeria_state[0]} {nigeria_state[-1]}")
print("Lagos" in nigeria_state)
print(len(nigeria_state))

# 4. Tuple Unpacking
user = [
        input("Enter your First Name: "),
        input("How old are you: "),
        input("What is your favourite color: "),
        input("Your Home Town: ")
]
profile = tuple(user)
print(profile)

name, age, favourite_color, home_town = profile[0], profile[1], profile[2], profile[3]
print(f"Name\t Age\t Favoure_Color\tHome_Town")
print(f"{name}\t {age}\t {favourite_color}\t        {home_town}")

# 5. Modifying tuple indirectly
shopping_tuple = (
                    input("Enter first shopping item: "),
                    input("Enter second shopping item: "),
                    input("Enter third shopping item: ")   
)
shopping_list = list(shopping_tuple)
print(shopping_list)
add_item = [
                input("Enter fourth shopping item: "),
                input("Enter fifth shopping item: ")
]
print(add_item)
total_item = shopping_list + add_item
print(total_item)
total_item_in_tuple = tuple(total_item)
print("|".join(total_item_in_tuple))
'''
# Attendance Tracker
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
months = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

name = input("Enter Student's name: ")
gender = input("What is your Gender: ")
course_track = input("What is your Course Track: ")
month = int(input("Current month number (1-12): "))
day = int(input("current day number(1-7): "))
print(f"{name}")
print(f"{gender}")
print(f"{course_track}")
print(days[day - 1])
print(months[month - 1])