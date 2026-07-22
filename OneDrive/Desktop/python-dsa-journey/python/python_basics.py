# PYTHON BASICS PRACTICE
# Learning: Variables, Data Types, Input, Type Conversion, and Operators

# -----------------------------
# VARIABLES
# -----------------------------
city = "Bidar"
print(city)

city = "Bengaluru"
print(city)

name = "Ganga"
friend = name
name = "Engineer Ganga"

print(name)
print(friend)

# -----------------------------
# DATA TYPES
# -----------------------------
name = "Ganga"      # String
age = 20             # Integer
sgpa = 8.5           # Float
is_student = True    # Boolean

print(name)
print(age)
print(sgpa)
print(is_student)

# -----------------------------
# INPUT AND TYPE CONVERSION
# -----------------------------
name = input("Enter your name: ")
age = int(input("Enter your age: "))
sgpa = float(input("Enter your SGPA: "))

print("Name:", name)
print("Age:", age)
print("SGPA:", sgpa)

print(type(age))
print(type(sgpa))

# -----------------------------
# OPERATORS
# -----------------------------
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum_result = a + b
difference = a - b
multiplication = a * b
division = a / b
remainder = a % b
floor_division = a // b
power = a ** b

print("Sum:", sum_result)
print("Difference:", difference)
print("Multiplication:", multiplication)
print("Division:", division)
print("Remainder:", remainder)
print("Floor Division:", floor_division)
print("Power:", power)