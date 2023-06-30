# Snack Inventory Management System

# Initialize inventory and sales record
inventory = []
sales_record = []

# Function to add a snack to the inventory
def add_snack():
    snack_id = input("Enter snack ID: ")
    snack_name = input("Enter snack name: ")
    snack_price = float(input("Enter snack price: "))
    snack_available = input("Is the snack available? (yes/no): ")

    snack = {
        "ID": snack_id,
        "Name": snack_name,
        "Price": snack_price,
        "Available": snack_available.lower() == "yes"
    }

    inventory.append(snack)
    print("Snack added successfully!")

# Function to remove a snack from the inventory
def remove_snack():
    snack_id = input("Enter snack ID to remove: ")

    for snack in inventory:
        if snack["ID"] == snack_id:
            inventory.remove(snack)
            print("Snack removed successfully!")
            return

    print("Snack not found in inventory!")

# Function to update the availability of a snack
def update_availability():
    snack_id = input("Enter snack ID to update availability: ")

    for snack in inventory:
        if snack["ID"] == snack_id:
            snack["Available"] = not snack["Available"]
            print("Availability updated successfully!")
            return

    print("Snack not found in inventory!")

# Function to record a snack sale
def record_sale():
    snack_id = input("Enter snack ID sold: ")

    for snack in inventory:
        if snack["ID"] == snack_id:
            if snack["Available"]:
                sales_record.append(snack)
                snack["Available"] = False
                print("Sale recorded successfully!")
                return
            else:
                print("Snack is not available for sale!")
                return

    print("Snack not found in inventory!")

# Function to display the inventory
def display_inventory():
    print("\nSnack Inventory:")
    for snack in inventory:
        print("ID:", snack["ID"])
        print("Name:", snack["Name"])
        print("Price:", snack["Price"])
        print("Available:", "Yes" if snack["Available"] else "No")
        print("-----------------------")
    print()

# Function to display the sales record
def display_sales_record():
    print("\nSales Record:")
    for snack in sales_record:
        print("ID:", snack["ID"])
        print("Name:", snack["Name"])
        print("Price:", snack["Price"])
        print("-----------------------")
    print()

# Main program loop
while True:
    print("Welcome to Mumbai Munchies: The Canteen Chronicle!")
    print("1. Add Snack to Inventory")
    print("2. Remove Snack from Inventory")
    print("3. Update Snack Availability")
    print("4. Record Snack Sale")
    print("5. Display Inventory")
    print("6. Display Sales Record")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_snack()
    elif choice == "2":
        remove_snack()
    elif choice == "3":
        update_availability()
    elif choice == "4":
        record_sale()
    elif choice == "5":
        display_inventory()
    elif choice == "6":
        display_sales_record()
    elif choice == "0":
        break
    else:
        print("Invalid choice! Please try again.")

print("Thank you for using Mumbai Munchies: The Canteen Chronicle!")
