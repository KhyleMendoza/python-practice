##Strings
# name = "Khyle"
# print("Hello ", name)
# print("Hello " + name)
# print(f"Hello {name}")

##Integers
# age = 22
# print(f"Your age is {age} years old")
# quantity = 5
# print(f"You are buying {quantity} items")

##Float
# price = 99.9999
# quantity = 3
# print(f"The price is {price}.")
# print(f"Your total is {price * quantity}.")
# #display 2 digits only from float
# print(f"The price is {price:.2f}.")
# print(f"Your total is {price * quantity:.2f}.")

##Boolean
# is_student = True
# print(f"Are you a student? {is_student}")
# price = 100
# if is_student:
#     price = price * 0.8
#     print(f"The price is {price} discounted 20% off.")
# else:
#     print(f"The price is {price} no discount.")

##List
# shopping_list = ["banana", "bread", "milk", "egg", "pizza"]
# print(shopping_list)
# print(f"The length of the list is {len(shopping_list)}")
# print(f"the third item in the list is {shopping_list[2]}")
# shopping_list.append("apple")
# print("Adding apple to the list")
# print(shopping_list)
# shopping_list.insert(2, "orange")
# print("Added orange to the list")
# print(shopping_list)
# shopping_list.remove("milk")
# print("Removing milk from the list")
# print(shopping_list)
# shopping_list.pop()
# print("Removing the last item from the list")
# print(shopping_list)
# shopping_list.pop(2)
# print("Removing the item at index 2")
# print(shopping_list)
# shopping_list.sort()
# print("Sorting the list")
# print(shopping_list)
# shopping_list.reverse()
# print("Reversing the list")
# print(shopping_list)
# shopping_list.clear()
# print("Clearing the list")
# print(shopping_list)
# shopping_list.append("pizza")
# print("Adding pizza to the list")
# print(shopping_list)

#dictionary
# inventory = {
#     "apple": 10,
#     "banana": 20,
#     "orange": 30,
#     "pineapple": 40,
#     "mango": 50
# }

# print("Inventory: ", inventory)
# print(f"The length of the inventory is {len(inventory)}")
# print(f"The amount of the apple we have is {inventory['apple']}")
# inventory["apple"] = 100
# print("updated apple to 100")
# print("Inventory: ", inventory)
# inventory["banana"] += 10
# print("added 10 bananas")
# print("Inventory: ", inventory)
# inventory["orange"] -= 10
# print("removed 10 oranges")
# print("Inventory: ", inventory)
# inventory["pineapple"] *= 2
# print("doubled the amount of pineapples")
# print("Inventory: ", inventory)
# inventory["mango"] /= 2
# print("halved the amount of mangoes")
# print("Inventory: ", inventory)
# inventory.pop("mango")
# print("removed mango from the inventory")
# print("Inventory: ", inventory)
# inventory.clear()
# print("cleared the inventory")
# print("Inventory: ", inventory)
# inventory["strawberry"] = 10
# print("added strawberry with value 10")
# print("Inventory: ", inventory)

##Typecasting
# name="Khyle"
# age=22
# gpa=3.5
# is_student=True
##check type of variables
# print(f"Name: {type(name)}, Age: {type(age)}, GPA: {type(gpa)}, Is Student: {type(is_student)}")
##convert float to int, int to float, bool to str
# gpa = int(gpa)
# print(f"GPA: {gpa}")
# age=float(age)
# print(f"Age: {age}")
# is_student=str(is_student)
# print(f"Is Student: {is_student}")
# name = bool(name)
# print(f"Name: {name}")
##check type of variables
# print(f"Name: {type(name)}, Age: {type(age)}, GPA: {type(gpa)}, Is Student: {type(is_student)}")

# #input
# name = input("Enter your name: ")
# print(f"Hello {name}!")
# #v1 of getting input of age
# age = input("Enter your age: ")
# print(f"Your age is {age} years old!")
# age = int(age)
# age = age + 1
# print(f"Your age increase by 1 year you are now {age} years old!")

# #v2 more readable compare to v1 of getting input of age
# age = int(input("Enter your age: "))
# print(f"Your age is {age} years old!")
# age = age + 1
# print(f"Your age increase by 1 year you are now {age} years old!")

# #shop example
# item = input("Enter the name of the Item: ")
# price = float(input("Enter the price of the Item: "))
# Quantity = int(input("Enter the quantity of the Item: "))
# print(f"You have bought {Quantity} quantity of {item}")
# print(f"The total price of the Item is {price * Quantity}.")

#arithmetic operators
#++
#--
#+=
#-=
#*=
#/=
#=
#==
#===
#!=
#>
#<
#>=
#<=
#and
#or
#not

# balance = 0
# balance = balance + 100
# print(f"Your balance is {balance}")
# balance += 100
# print(f"Your balance is {balance}")
# balance -= 50
# print(f"Your balance is {balance}")
# balance *= 2
# print(f"Your balance is {balance}")
# balance /= 2
# print(f"Your balance is {balance}")

##if statement
# if balance >= 100:
#     print("You are rich")
# elif balance > 0 and balance <= 99:
#     print("You are middle class")
# else:
#     print("You are broke")

# #calculator example
# operation = input("Enter the operation(+, -, *, /): ")
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# if operation == "+":
#     print(f"{num1 + num2}")
# elif operation == "-":
#     print(f"{num1 - num2}")
# elif operation == "*":
#     print(f"{num1 * num2}")
# elif operation == "/":
#     print(f"{num1 / num2}")
# else:
#     print("Invalid Operation!")

##while loop
# while True:
#     print("Welcome to shop")
#     print("1. Pizza - 100")
#     print("2. burger - 50")
#     print("3. Exit")
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         print("You bought a pizza")
#     elif choice == "2":
#         print("You bought a Burger")
#     elif choice == "3":
#         print("Thank you for visiting!")
#         break
#     else:
#         print("Invalid Choice! Please try again")

#for loop
# for i in range(10):
#     print(i)

# #product example using list
# products = ["laptop", "mouse", "keyboard", "monitor", "headphones"]
# print("Available products:")
# for product in products:
#     print(f"{product}")

# #product example with price using dictionary
# products = {
#     "laptop": 15000,
#     "mouse": 500,
#     "keyboard": 1500,
#     "monitor": 3000,
#     "headphones": 1000,
# }
# print("Available products: ")
# for product, price in products.items():
#     print(f"{product}: ₱{price}")

# #function
# def hello():
#     print("Hello")

# hello()

# #function with parameter
# def greet(name):
#     return f"Hello {name}!"

# name = input("Enter your name: ")
# print(greet(name))

# #function with default parameter
# def greet(name="Khyle"):
#     return f"Hello {name}!"

# print(greet())

# # Classes
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
    
#     def display(self):
#         print(f"{self.name}: ₱{self.price}")

# laptop = Product("Laptop", 15000)
# mouse = Product("mouse", 1000)
# laptop.display()
# mouse.display()

##single product example
# name = input("Enter product name: ")
# price = float(input("Enter product price: "))
# product = Product(name, price)
# product.display()

##multiple product example
# products = {
#     "laptop": 15000,
#     "mouse": 1000,
#     "keyboard": 1500,
# }

# print("Current products:")
# for name, price in products.items():
#     print(f"{name}: ₱{price}")

# name = input("Enter product name: ")
# price = float(input("Enter product price: "))
# products[name.lower()] = price

# print("\nUpdated products:")
# for name, price in products.items():
#     print(f"{name}: ₱{price}")

# # Multiple products using class
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
    
#     def display(self):
#         print(f"{self.name}: ₱{self.price}")

# products = [
#     Product("Laptop", 15000),
#     Product("Mouse", 1000),
#     Product("Keyboard", 1500)
# ]

# print("Current products:")
# for product in products:
#     product.display()

# name = input("Enter product name: ")
# price = float(input("Enter product price: "))
# new_product = Product(name, price)
# products.append(new_product)

# for product in products:
#     product.display()