# Simple Inventory Management System
inventory = [] 

while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Product")
    print("2. View All Products")
    print("3. Search Product by Name")
    print("4. Update Product Quantity")
    print("5. Delete Product")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Product Name: ")
        qty = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        inventory.append({"name": name, "qty": qty, "price": price})
        print("Product added successfully!")

    elif choice == 2:
        print("\n--- Product List ---")
        for p in inventory:
            print(f"Name: {p['name']}, Qty: {p['qty']}, Price: {p['price']}")

    elif choice == 3:
        search = input("Enter Product Name to search: ")
        found = False
        for p in inventory:
            if p['name'].lower() == search.lower():
                print(f"Found → Name: {p['name']}, Qty: {p['qty']}, Price: {p['price']}")
                found = True
        if not found:
            print("Product not found.")

    elif choice == 4:
        update = input("Enter Product Name to update: ")
        for p in inventory:
            if p['name'].lower() == update.lower():
                new_qty = int(input("Enter new quantity: "))
                p['qty'] = new_qty
                print("Quantity updated successfully!")
                break
        else:
            print("❌ Product not found.")

    elif choice == 5:
        delete = input("Enter Product Name to delete: ")
        for p in inventory:
            if p['name'].lower() == delete.lower():
                inventory.remove(p)
                print("Product deleted successfully!")
                break
        else:
            print("Product not found.")

    elif choice == 6:
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
