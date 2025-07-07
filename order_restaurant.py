# the items has been written and categorised as according to the types..in list type
menu = {
    "pizza": {"cheeze": 120, "pepperoni": 150, "veggie": 100},
    "coffee": {"black": 50, "latte": 70, "cappuccino": 80},
    "burger": {"chicken": 60, "veggie": 50},
    "pasta": {"alfredo": 90, "marinara": 80},
    "cold drinks": {"soda": 30, "juice": 40, "water": 20}
}
# mostly ordered items has been mentioned in list form only..
mostly_ordered = {"cheese": 120, "cappuccino": 80, "chicken burger": 60}

#this shows total bill starts from zero.
total_bill = 0
order_summary=[]

#  Ask if user wants to see menu or famous
a = input("Hello sir,\nWould you like to see the 'menu' or 'mostly ordered' items?\n").lower()

# if satements are used if options are their for example in this case 
# if cousterm uses mostly or famous world while asking the answer it wil print the next comand given ..

if "mostly" in a or "famous" in a:
    print("\nHere you go sir, the mostly ordered items are:")

    for item, price in mostly_ordered.items():
        #shows mostly ordered items nicely and with price..
        # f string is used as more 1 one function has to be performed by it .
        print(f"- {item.title()} : ₹{price}")

if "menu" in a:
    print("\n Full Menu:")
    for category, items in menu.items():
        print(f"\n{category.title()}:")
        for item, price in items.items():
            print(f"  - {item.title()} : ₹{price}")
# .lower() is used so that if the user write category either in upper or lower or mixed case it can interpret easily..
category1 = input("\nEnter category for Order 1: ").lower()

# check if category exists in menu
if category1 in menu:
    #[] type of bracket used as category1 is inside a menu ,is used when comand of one fucntion is inside other ..
    print("here you go sir", menu[category1])
    item1 = input("Enter item you want to order: ").lower()
    if item1 in menu[category1]:
        quantity1 = int(input(f"number of {item1} you want to order? "))
        price1 = menu[category1][item1]
        subtotal1 = price1 * quantity1
        # += sign used to endicate the equal to sign for command 
        total_bill += subtotal1
        # .append() merges all the things u need to print..
        order_summary.append((item1, quantity1, price1, subtotal1))
        print(f"{quantity1} x {item1.title()} added to your order.")
    else:
        print(" This item is not available.")
else:
    print("Category not found.")

# -------- Second Order ......
order2 = input("\nWould you like to order something else? (yes/no): ").lower()

if order2 == "yes":
    category2 = input("Enter category for Order 2: ").lower()
    if category2 in menu:
        print("Available items:", menu[category2])
        item2 = input("Enter item you want to order: ").lower()
        if item2 in menu[category2]:
            quantity2 = int(input(f"How many {item2} would you like to order? "))
            price2 = menu[category2][item2]
            subtotal2 = price2 * quantity2
            total_bill += subtotal2
            order_summary.append((item2, quantity2, price2, subtotal2))
            print(f"{quantity2} x {item2.title()} added to your order.")
        else:
            print(" Item not found.")
    else:
        print("Category not found.")

# -------- Order Summary --------
print("\n Order Summary:")
print("Item\t\tQty\tPrice\tSubtotal")
#-*30 here 30 means i want "-" 30 times.. which will help me to print the table...
print("-" * 30)
for item, qty, price, subtotal in order_summary:
    #\t ,is used to give a tab type space between the items writeen 
    print(f"{item.title():10s}\t{qty}\t₹{price}\t₹{subtotal}")
print("-" * 30)
print(f"Total Bill:\t\t\t₹{total_bill}")
#\n used to add new line and the result will be clean..
print("\n Thank you for ordering with us!")
print("👋 Have a good day, sir!")
