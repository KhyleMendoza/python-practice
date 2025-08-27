import json
import os
from datetime import datetime

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class POS:
    def __init__(self):
        self.products = {}
        self.admin_password = "admin123"
        self.cart = {}
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.products_file = os.path.join(self.script_dir, 'products.json')
        self.load_products()
    
    def load_products(self):
        if os.path.exists(self.products_file):
            try:
                with open(self.products_file, 'r') as f:
                    data = json.load(f)
                    self.products = data
            except:
                self.products = {}
        else:
            self.products = {
                "1": {"name": "Bread", "price": 25.00, "stock": 20},
                "2": {"name": "Milk", "price": 30.00, "stock": 15},
                "3": {"name": "Eggs", "price": 45.00, "stock": 30}
            }
            self.save_products()
    
    def save_products(self):
        with open(self.products_file, 'w') as f:
            json.dump(self.products, f, indent=4)
    
    def admin_login(self):
        attempts = 3
        while attempts > 0:
            password = input("Enter admin password: ")
            if password == self.admin_password:
                print("Login successful!")
                return True
            else:
                attempts -= 1
                print(f"Invalid password. {attempts} attempts remaining.")
        print("Too many failed attempts. Returning to main menu.")
        return False
    
    def admin_menu(self):
        while True:
            print("\n=== ADMIN MENU ===")
            print("1. Add Product")
            print("2. Update Product Price")
            print("3. Update Product Stock")
            print("4. Remove Product")
            print("5. View All Products")
            print("6. Logout")
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.update_price()
            elif choice == "3":
                self.update_stock()
            elif choice == "4":
                self.remove_product()
            elif choice == "5":
                self.view_all_products()
            elif choice == "6":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def add_product(self):
        print("\n=== ADD PRODUCT ===")
        name = input("Enter product name: ")
        try:
            price = float(input("Enter product price: ₱"))
            stock = int(input("Enter initial stock: "))
            
            product_id = str(len(self.products) + 1)
            while product_id in self.products:
                product_id = str(int(product_id) + 1)
            
            self.products[product_id] = {
                "name": name,
                "price": price,
                "stock": stock
            }
            self.save_products()
            print(f"Product '{name}' added successfully with ID: {product_id}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    
    def update_price(self):
        print("\n=== UPDATE PRODUCT PRICE ===")
        self.view_all_products()
        
        product_id = input("Enter product ID to update: ")
        if product_id in self.products:
            try:
                new_price = float(input("Enter new price: ₱"))
                self.products[product_id]["price"] = new_price
                self.save_products()
                print(f"Price updated successfully for {self.products[product_id]['name']}")
            except ValueError:
                print("Invalid price. Please enter a valid number.")
        else:
            print("Product not found.")
    
    def update_stock(self):
        print("\n=== UPDATE PRODUCT STOCK ===")
        self.view_all_products()
        
        product_id = input("Enter product ID to update: ")
        if product_id in self.products:
            try:
                new_stock = int(input("Enter new stock quantity: "))
                self.products[product_id]["stock"] = new_stock
                self.save_products()
                print(f"Stock updated successfully for {self.products[product_id]['name']}")
            except ValueError:
                print("Invalid stock quantity. Please enter a valid number.")
        else:
            print("Product not found.")
    
    def remove_product(self):
        print("\n=== REMOVE PRODUCT ===")
        self.view_all_products()
        
        product_id = input("Enter product ID to remove: ")
        if product_id in self.products:
            product_name = self.products[product_id]["name"]
            confirm = input(f"Are you sure you want to remove '{product_name}'? (y/n): ")
            if confirm.lower() == 'y':
                del self.products[product_id]
                self.save_products()
                print(f"Product '{product_name}' removed successfully.")
        else:
            print("Product not found.")
    
    def view_all_products(self):
        print("\n=== ALL PRODUCTS ===")
        if not self.products:
            print("No products available.")
            return
        
        print(f"{'ID':<5} {'Name':<20} {'Price':<10} {'Stock':<10}")
        print("-" * 45)
        for product_id, product in self.products.items():
            print(f"{product_id:<5} {product['name']:<20} ₱{product['price']:<9} {product['stock']:<10}")
    
    def customer_menu(self):
        self.cart = {}
        
        while True:
            print("\n=== CUSTOMER MENU ===")
            print("1. View Products")
            print("2. Add to Cart")
            print("3. View Cart")
            print("4. Remove from Cart")
            print("5. Checkout")
            print("6. Back to Main Menu")
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == "1":
                self.view_products_customer()
            elif choice == "2":
                self.add_to_cart()
            elif choice == "3":
                self.view_cart()
            elif choice == "4":
                self.remove_from_cart()
            elif choice == "5":
                self.checkout()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def view_products_customer(self):
        print("\n=== AVAILABLE PRODUCTS ===")
        if not self.products:
            print("No products available.")
            return
        
        print(f"{'ID':<5} {'Name':<20} {'Price':<10} {'Stock':<10}")
        print("-" * 45)
        for product_id, product in self.products.items():
            if product['stock'] > 0:
                print(f"{product_id:<5} {product['name']:<20} ₱{product['price']:<9} {product['stock']:<10}")
    
    def add_to_cart(self):
        self.view_products_customer()
        
        product_id = input("Enter product ID to add to cart: ")
        if product_id in self.products:
            if self.products[product_id]['stock'] > 0:
                try:
                    quantity = int(input("Enter quantity: "))
                    if quantity <= self.products[product_id]['stock']:
                        if product_id in self.cart:
                            self.cart[product_id] += quantity
                        else:
                            self.cart[product_id] = quantity
                        print(f"Added {quantity} {self.products[product_id]['name']} to cart.")
                    else:
                        print("Not enough stock available.")
                except ValueError:
                    print("Invalid quantity. Please enter a valid number.")
            else:
                print("Product is out of stock.")
        else:
            print("Product not found.")
    
    def view_cart(self):
        print("\n=== YOUR CART ===")
        if not self.cart:
            print("Your cart is empty.")
            return
        
        total = 0
        print(f"{'Name':<20} {'Price':<10} {'Qty':<5} {'Subtotal':<10}")
        print("-" * 45)
        
        for product_id, quantity in self.cart.items():
            product = self.products[product_id]
            subtotal = product['price'] * quantity
            total += subtotal
            print(f"{product['name']:<20} ₱{product['price']:<9} {quantity:<5} ₱{subtotal:<9.2f}")
        
        print("-" * 45)
        print(f"Total: ₱{total:.2f}")
    
    def remove_from_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        
        self.view_cart()
        product_id = input("Enter product ID to remove from cart: ")
        
        if product_id in self.cart:
            try:
                quantity = int(input("Enter quantity to remove: "))
                if quantity >= self.cart[product_id]:
                    del self.cart[product_id]
                    print("Item removed from cart.")
                else:
                    self.cart[product_id] -= quantity
                    print(f"Removed {quantity} from cart.")
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")
        else:
            print("Product not in cart.")
    
    def checkout(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        
        print("\n=== CHECKOUT ===")
        self.view_cart()
        
        confirm = input("Proceed with purchase? (y/n): ")
        if confirm.lower() == 'y':
            for product_id, quantity in self.cart.items():
                self.products[product_id]['stock'] -= quantity
            
            self.save_products()
            self.generate_receipt()
            self.cart = {}
            print("Purchase completed successfully!")
    
    def generate_receipt(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"receipt_{timestamp}.txt"
        receipt_path = os.path.join(self.script_dir, filename)
        
        with open(receipt_path, 'w') as f:
            f.write("=== RECEIPT ===\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("-" * 30 + "\n")
            
            total = 0
            for product_id, quantity in self.cart.items():
                product = self.products[product_id]
                subtotal = product['price'] * quantity
                total += subtotal
                f.write(f"{product['name']} x{quantity} @₱{product['price']:.2f} = ₱{subtotal:.2f}\n")
            
            f.write("-" * 30 + "\n")
            f.write(f"Total: ₱{total:.2f}\n")
            f.write("Thank you for your purchase!\n")
        
        print(f"Receipt saved as {filename}")

def main():
    pos = POS()
    
    while True:
        print("\n=== POS SYSTEM ===")
        print("1. Admin Login")
        print("2. Customer Shopping")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            if pos.admin_login():
                pos.admin_menu()
        elif choice == "2":
            pos.customer_menu()
        elif choice == "3":
            print("Thank you for using the POS system!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()