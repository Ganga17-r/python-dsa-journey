# Python Day 2 - Variables, Data Types, Input and Operators

# Variables and Data Types
name = "Ganga"
age = 20
sgpa = 8.5
is_student = True

print(name)
print(age)
print(sgpa)
print(is_student)

print(type(name))
print(type(age))
print(type(sgpa))
print(type(is_student))

# User Input
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_sgpa = float(input("Enter your SGPA: "))

print("Name:", user_name)
print("Age:", user_age)
print("SGPA:", user_sgpa)

# Basic Operators
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Remainder:", a % b)
print("Floor Division:", a // b)
print("Power:", a ** b)