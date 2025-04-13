# def greet():
#     print("Hello, How can I help you?")
# greet()

# def user_input():
#     print("Please enter your name: ")
#     name = input()                             #input name
#     print("Please enter your age: ")
#     age = input()                              #input age
#     return name, age                           #value return
# user_input()                                   #call

# def name_printer(name):
#     print("Hello, "+name,"how can I help you?")
# name_printer("Rahul Jaiswal")
# name_printer("Ravi Kumar")

# # Calculate a multiplication of number
# def malti():
#     number1 =int(input("Enter a number: "))
#     number2 = int(input("Enter another number: "))
#     return number1*number2
# result = malti()
# print(result)

# calculate square of number
# def square(number):                               #variable
#     number1=int(input("Enter the  number: "))
#     return number1**number
# result=square(2)                     #hold the value
# print(result)


# calculate the Cube(3) of number
# def cube(num):
#     number1 =int(input("Enter the number which find the cube: "))
#     return number1**num
# result = cube(3)
# print(result)

# calculate and add two numbers but input from user
# def add():
#     number1=int(input("Enter the first number: "))
#     number2=int(input("Enter the second number: "))
#     return number1+number2
# Jodo=add()
# print("Sum of two number :",Jodo)


#  Write a function multiply that multiplies two numbers, but can also accept and multiply String(polymorphism)
# def multiply():
#     number = int(input("Enter a number: "))
#     word =input("Enter a word: ")
#     return number*word
# result = multiply()
# print(result)

# Default parameter value
# Write a function that greets a user. If no name is provided, it should greet with a default name.
# def greet(name = "User"):
#     return "hello, " + name + "!"
# result = greet("Rahul")
# print(result)
# print(greet())

# def greet():
#     greeting = "Hello, "
#     name = input("What is your name?:")
#     return greeting + name
# result = greet()
# print(result)

# lambda function
# find out cube of a number
# cube = lambda x: x**3
# print(cube(5))

# num1 = int(input("Enter the  number: "))
# cube = lambda num1: num1**3
# print(cube(num1))

# calculate Gmean

# def calculate_gmean(a,b):
#     return (a*b)/(a+b)
# result = calculate_gmean(1,2)
# print(result)

# show the which is grater or less than
# def big_small():
#     number1 = int(input("Enter 1st number: "))
#     number2 = int(input("Enter 2nd number: "))
#     if number1 > number2:
#         return f"{number1} is Grater Than {number2} number"
#     elif number1 < number2:
#         return f"{number2} is  Grater Than {number1} number"
#     else:
#         return f"{number1} and {number2} is  Equal Number"
# result = big_small()
# print(result)

# Function inside function

# def big_small():
#     number1 = int(input("Enter 1st number: "))
#     number2 = int(input("Enter 2nd number: "))
#     def check(a, b):
#       if a > b :
#         return f"{a} is Grater Than {b} number"
#       elif a < b:
#         return f"{b} is Grater Than {a} number"
#       else:
#         return f"{a} and {b} is  Equal Number"
#     result = check(number1, number2)
#     return result
# output = big_small()
# print(output)

