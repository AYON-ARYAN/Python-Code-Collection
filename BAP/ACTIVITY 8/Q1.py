class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Item: {self.name}, Price: {self.price}, Quantity: {self.quantity}")


class Customer:
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def display_info(self):
        print(f"Customer: {self.name}, Email: {self.num}")


class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.customers = []

    def add_product(self, product):
        self.products.append(product)

    def add_customer(self, customer):
        self.customers.append(customer)

    def display_products(self):
        print(f"Products available at {self.name}:")
        for product in self.products:
            product.display_info()

    def display_customers(self):
        print(f"Customers of {self.name}:")
        for customer in self.customers:
            customer.display_info()

    def sell_product(self, product_name, customer_name):
        for product in self.products:
            if product.name == product_name:
                if product.quantity > 0:
                    print(f"{product_name} sold to {customer_name} for ${product.price}")
                    product.quantity -= 1
                    return
                else:
                    print(f"Sorry, {product_name} is out of stock.")
                    return
        print(f"Sorry, {product_name} not found in the store.")

    def add_inventory(self, product_name, quantity):
        for product in self.products:
            if product.name == product_name:
                product.quantity += quantity
                print(f"Added {quantity} units of {product_name} to inventory.")
                return
        print(f"Sorry, {product_name} not found in the store.")


if __name__ == "__main__":
    notebook = Product("Notebook", 10, 10)
    battery = Product("Battery", 5, 20)
    apple = Product("Apple", 2, 20)
    mango = Product("Mango", 3, 15)
    eggs = Product("Eggs", 1, 30)

    customer1 = Customer("AVI", "99462534735")
    customer2 = Customer("AAYUSH", "7023121160")

    store = Store("GENERAL_STORE")

    store.add_product(notebook)
    store.add_product(battery)
    store.add_product(apple)
    store.add_product(mango)
    store.add_product(eggs)
    store.add_customer(customer1)
    store.add_customer(customer2)

    store.display_products()
    print()
    store.display_customers()
    print()

    while True:
        choice = input("Do you want to buy a product? (yes/no): ")
        if choice.lower() == 'no':
            break
        elif choice.lower() == 'yes':
            product_name = input("Enter the name of the product you want to buy: ")
            customer_name = input("Enter your name: ")
            store.sell_product(product_name, customer_name)

    print("\nUpdated Inventory:")
    store.display_products()
