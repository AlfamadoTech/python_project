# Online Store Cart Calculation
list_of_items = ["Book", "Pen", "Bag", "Flask"]
price_of_items = [500, 200, 3000, 5000]
cart_total = 0
list_price = dict(zip(list_of_items, price_of_items))
pick_item = input("Pick item from list of item into cart: ").split(", ")
for pick_item in list_of_items:
    value = price_of_items
    cart_total += value
    print(f"Items: {pick_item} \n Total Price: {cart_total}")
'''if pick_item in list_of_items:
    value = list_price[pick_item]
    cart_total += value
    print(f"Items: {pick_item} \n Total Price: {cart_total}")

list_price = dict(zip(list_of_items, price_of_items))
pick_item = input("Pick item from list of item into cart: ").split(", ")
for pick_item in list_price:
    cart_total = sum(pick_item.values())
    print(f"Items: {pick_item} \n Total Price: {cart_total}")
'''