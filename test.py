import time
import os
import json
from datetime import datetime, timedelta

#loop
# pizza = 100
# slice = 0
# while pizza > 0:
#     pizza-=1
#     print("hello" + str(pizza))
#     time.sleep(1)

#if else statement
# if pizza > 0:
#     print("hello pizzaaa")
# elif pizza == 0:
#     print("no pizza")

#class input and output
# class Person:
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#     def say_hello(self):
#         return f"Hello, my name is {self.name} and i am {self.age} year old and i live in {self.city}."
    
#     def get_info(self):
#         return f"{self.name}, {self.age}, {self.city}"
    
# name = input("Enter your name: ")
# while True:
#     try:
#         age = int(input("Enter your age: "))
#         break
#     except ValueError:
#         print("Enter your age as a number!")


# city = input("Enter your city: ")

# person = Person(name, age, city)
# print(person.say_hello())
# time.sleep(1)
# print(person.get_info())

#function
# def pizzacount(pizza):
#     print("pizza " + str(pizza))

# pizza -=5
# pizzacount(str(pizza))

# for slice in range(100):
#     print("pizza slice =" + str(slice))

#list
# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")
# print(fruits)
# fruits.remove("banana")
# print(fruits)
# fruits[1] = "mango"
# print(fruits)

#dictionary
# person = {"name": "khyle", "age": 22, "city": "mabalacat"}
# print("my name is " + person["name"] + " and i am " + str(person["age"]) + " years old and im from " + person["city"] +".")

#tuple
# coordinate = (10, 20)
# print(coordinate[0])

#set
# numbers = {1, 2, 3, 4, 5}
# reversed_numbers = list(reversed(list(numbers)))
# print("original numbers: " + str(numbers))
# print("reversed numbers: " + str(reversed_numbers))
# new_numbers = list(numbers)
# new_numbers.reverse()
# print("reversed new numbers: " + str(new_numbers))

#list comprehension
# squares = [x**2 for x in range(10)]
# print(squares)

# even_numbers = [x for x in range(21) if x % 2 == 0]
# print(even_numbers)

# odd_numbers = [x for x in range(22) if x % 2 != 0]
# print(odd_numbers)



#exception handling try and except
# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print(result)
# except ValueError:
#     print("That's not a valid number!")
# except ZeroDivisionError:
#     print("You can't divide by zero!")

#file handling
# with open("test.txt", "w") as file:
#     file.write("hello world! \n")
#     file.write("hello world! \n")
#     file.write("hello world!")

# with open("test.txt", "r") as file:
#     content = file.read()
#     print(content)

#check if file exists
# if not os.path.exists("test1.txt"):
#     with open("test1.txt", "w") as file:
#         file.write("this is new file")
# else:
#     print("file already exists")

#create file with user input
# filename = input("Enter file name: ")
# content = input("Enter content for the file: ")

# with open(filename, "w") as file:
#     file.write(content)
#     file.write("\n write with python.")
# print(f"File '{filename}' Created Successfully!")

#create file with json
# person = {"name": "khyle", "age": 22, "city": "Mabalacat"}
# json_string = json.dumps(person)

# with open("person.json", "w") as file:
#     json.dump(person, file)

# with open("person.json", "r") as file:
#     data = json.load(file)
#     print(data)

#current date and time
# now = datetime.now()
# print("Current date and time: ", now)

# tommorow = now + timedelta(days=1)
# print("Tommorow Date and time: ", tommorow)

# last_week = now - timedelta(weeks=1)
# print("Last week date and time: ", last_week)

# date_string = "2025-08-26"
# parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
# print("Parsed Date: ", parsed_date)

