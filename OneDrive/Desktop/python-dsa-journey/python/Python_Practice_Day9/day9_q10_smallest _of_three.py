#Problem Statement
'''Write a Python program that asks the user to enter three numbers.

The program should print:

Smallest number is: __'''
num1=int(input("Enter your number:"))
num2=int(input("Enter your number:"))
num3=int(input("Enter your number:"))

if num1<=num2 and num1<=num3:
    print("smallest number:",num1)
elif num2<=num1 and num2<=num3:
    print("smallest number:", num2)
elif num3<=num1 and num3<=num2:
    print("smallest number:",num3)