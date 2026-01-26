import datetime

items = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5,
    "Eraser": 3,
    "Marker": 20
}

cart = {}

print("------ Welcome to Stationery Shop ------")
print("Available items:")
for item, price in items.items():
    print(f"{item:10} : Rs {price}")


while True:
    product = input("\nEnter item name (or 'done' to finish): ").capitalize()
    if product == "Done":
        break
    if product not in items:
        print("Item not available. Try again.")
        continue
    qty = int(input(f"Enter quantity of {product}: "))
    cart[product] = cart.get(product, 0) + qty

print("\n------ Final Bill ------")
print(f"Date: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
total = 0
for item, qty in cart.items():
    price = items[item]
    cost = price * qty
    total += cost
    print(f"{item:10} x {qty:<3} = Rs {cost:>5}")

gst = total * 0.05   
discount = 0
if total > 200:
    discount = total * 0.10   

grand_total = total + gst - discount

print("----------------------------")
print(f"Subtotal     : Rs {total}")
print(f"GST (5%)     : Rs {gst:.2f}")
print(f"Discount     : Rs {discount:.2f}")
print(f"Grand Total  : Rs {grand_total:.2f}")
print("----------------------------")
print("Thank you for shopping with us!")
