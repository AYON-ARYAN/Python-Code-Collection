import sqlite3

def create_table():
    conn = sqlite3.connect('/Volumes/DRIVE/BAP/ACTIVITY_7/Q1.db')
    dog = conn.cursor()
    dog.execute("""CREATE TABLE IF NOT EXISTS items_all (
                        ITEM_NAME TEXT,
                        ITEM_QUANTITY INTEGER,
                        ITEM_PRICE INTEGER
                    )""")
    conn.commit()
    conn.close()

def add_item():
    conn = sqlite3.connect('/Volumes/DR/3IVE/BAP/ACTIVITY_7/Q1.db')
    dog = conn.cursor()
    name = input("Enter the name of the item: ")
    quantity = int(input('Enter the quantity of the item: '))
    price = int(input("Enter the price of the item: "))
    dog.execute("INSERT INTO items_all (ITEM_NAME, ITEM_QUANTITY, ITEM_PRICE) VALUES (?, ?, ?)", (name, quantity, price))
    conn.commit()
    conn.close()

def update_quantity():
    conn = sqlite3.connect('/Volumes/DRIVE/BAP/ACTIVITY_7/Q1.db')
    dog = conn.cursor()
    name = input("Enter the name of the item to update quantity: ")
    new_quantity = int(input("Enter the new quantity: "))
    dog.execute("UPDATE items_all SET ITEM_QUANTITY = ? WHERE ITEM_NAME = ?", (new_quantity, name))
    conn.commit()
    conn.close()

def update_price():
    conn = sqlite3.connect('/Volumes/DRIVE/BAP/ACTIVITY_7/Q1.db')
    dog = conn.cursor()
    name = input("Enter the name of the item to update price: ")
    new_price = int(input("Enter the new price: "))
    dog.execute("UPDATE items_all SET ITEM_PRICE = ? WHERE ITEM_NAME = ?", (new_price, name))
    conn.commit()
    conn.close()

def view_items():
    conn = sqlite3.connect('/Volumes/DRIVE/BAP/ACTIVITY_7/Q1.db')
    dog = conn.cursor()
    dog.execute("SELECT * FROM items_all")
    items = dog.fetchall()
    for item in items:
        print("Name:", item[0])
        print("Quantity:", item[1])
        print("Price:", item[2])
    conn.close()

def bill():
    conn = sqlite3.connect('/Volumes/DRIVE/BAP/ACTIVITY_7/Q1.db')
    dog = conn.cursor()
    dog.execute("SELECT ITEM_NAME, ITEM_QUANTITY, ITEM_PRICE FROM items_all")
    items = dog.fetchall()
    total_bill = 0
    print("\nBilling Details:")
    print("----------------")
    for item in items:
        item_total = item[1] * item[2]
        print("Item:", item[0])
        print("Quantity:", item[1])
        print("Price per unit:", item[2])
        print("Total for this item:", item_total)
        total_bill += item_total
    print("\nTotal Bill:", total_bill)
    conn.close()

def main():
    create_table()
    while True:
        print("\n1. Add Item")
        print("2. Update Quantity")
        print("3. Update Price")
        print("4. View Items")
        print("5. Generate Bill")
        print("6. Exit")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            add_item()
        elif choice == 2:
            update_quantity()
        elif choice == 3:
            update_price()
        elif choice == 4:
            view_items()
        elif choice == 5:
            bill()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
