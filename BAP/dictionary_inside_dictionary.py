print("Welcome to brands")
brands = {}

def add_brand():
    brand_name = input("Enter brand name: ")
    brands[brand_name] = {}

def add_product():
    brand_name = input("Enter brand name: ")
    product_name = input("Enter product name: ")
    product_price = input("Enter product price: ")
    brands[brand_name][product_name] = product_price
   

def display_inventory():
    print("Current Inventory:")
    for brand, products in brands.items():
        print(f"\n{brand}:")
        for product, price in products.items():
            print(f"{product} - ${price}")
    
z=1
while z==1:
    print("\nMenu:")
    print("1. Add Brand")
    print("2. Add Product")
    print("3. Display Inventory")
    print("4. Exit")
        
    choice = input("Enter your choice: ")
        
    if choice == '1':
        add_brand()
    elif choice == '2':
        add_product()
    elif choice == '3':
        display_inventory()
    elif choice == '4':
        print("Exiting...")
        z+1
        break
    else:
        print("Invalid choice!")

