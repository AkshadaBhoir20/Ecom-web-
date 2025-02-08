from codecarbon import EmissionsTracker

tracker =EmissionsTracker()
tracker.start()

# Define a class to represent a Product
class Product:
    def __init__(self, id, name, price):
        # Initialize product with given id, name, and price
        self.id = id
        self.name = name
        self.price = price

# Define a class for ShoppingCart
class ShoppingCart:
    def __init__(self):
        # Initialize an empty list to store products in the cart
        self.products = []

    def add_product(self, product):
        # Add the given product to the cart
        self.products.append(product)
        print(f"{product.name} added to the cart.")

    def remove_product(self, product):
        # Remove the given product from the cart if it exists
        if product in self.products:
            self.products.remove(product)
            print(f"{product.name} removed from the cart.")
        else:
            print("Product not found in cart.")

    def calculate_total(self):
        # Calculate and return the total price of all products in the cart
        return sum(product.price for product in self.products)

    def display_cart(self):
        # Print the details of all products in the cart
        if not self.products:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for product in self.products:
                print(f"- {product.name}: ${product.price}")

# Define a class for Customer
class Customer:
    def __init__(self, name, email):
        # Initialize customer with name and email
        # Create an empty shopping cart for the customer
        self.name = name
        self.email = email
        self.cart = ShoppingCart()

    def add_to_cart(self, product):
        # Add a product to the customer’s shopping cart
        self.cart.add_product(product)

    def remove_from_cart(self, product):
        # Remove a product from the customer’s shopping cart
        self.cart.remove_product(product)

    def checkout(self):
        # Calculate total cost of items in cart
        # Display the total amount the customer needs to pay
        total = self.cart.calculate_total()
        print(f"Total amount to pay: ${total}")

# List of available products
products = [
    Product(1, "iPhone", 1000),
    Product(2, "Laptop", 1500),
    Product(3, "Headphones", 200),
    Product(4, "Smartwatch", 300)
]

# Create a customer object with a name and email
customer = Customer("John Doe", "johndoe@example.com")

print("Welcome to the e-commerce store!")
print("Here are some available products:")
for product in products:
    print(f"{product.id}. {product.name} - ${product.price}")

while True:
    print("\nSelect an option from below:")
    print("1. Add a product to the cart")
    print("2. Display cart")
    print("3. Remove a product from the cart")
    print("4. Checkout")
    user_input = input("Enter option number: ")

    if user_input == '1':
        product_id = int(input("Enter the product ID to add: "))
        product = next((p for p in products if p.id == product_id), None)
        if product:
            customer.add_to_cart(product)
        else:
            print("Invalid product ID. Please try again.")

    elif user_input == '2':
        customer.cart.display_cart()

    elif user_input == '3':
        product_id = int(input("Enter the product ID to remove: "))
        product = next((p for p in customer.cart.products if p.id == product_id), None)
        if product:
            customer.remove_from_cart(product)
        else:
            print("Invalid product ID. Please try again.")

    elif user_input == '4':
        customer.checkout()
        break
    
    else:
        print("Invalid option. Please try again.")


emissions = tracker.stop()
print(f"Estimated CO2 Emissions : {emissions}kg")