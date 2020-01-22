# Lab6.py
# takes a selection & adds the price to the total.
# selections range from 1 - 5.

product_list = [[1, "Truffle", 6.95], [2, "Roses", 12.95], [3, "Latte", 3.95], [4, "Gift Card", 15.000], [5, "Phone App", 0.990]]

cart = []
item_list = []
price_list = []
price = 0

for i in range (len(product_list)):
    item_chosen = product_list[i][1]
    item_list.append(item_chosen)

for i in range (len(product_list)):
    item_price = product_list[i][2]
    price_list.append(item_price)

request = "Enter the product number 1 - 5. Press 0 to cancel order or Return to Checkout. "

print ("Shopmart Valentine Specials!")
print (product_list)


product_number = input(request)
while product_number != "0" and product_number != "":
    index_number = int(product_number) - 1
    item_price = price_list[index_number]
    item_picked = item_list[index_number]
    print ("You ordered : " + item_picked)
    cart = cart + [item_picked]
    print (cart)
    price = price + item_price
    print ("Total is " + str(price))
    product_number = input (request)
if product_number == "":
    print ("Checkout: Please pay " + str(price))
else:
    print ("Have a good day!")
