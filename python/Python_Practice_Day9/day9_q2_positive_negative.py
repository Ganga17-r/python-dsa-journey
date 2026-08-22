#Problem-2

'''Write a program that asks the user to enter a number.
The program should print:
1 If the number is greater than 0
   Positive Number
2 If the number is less than 0
   Negative Number
3 Otherwise
   Zero'''
num=int(input("Enter your number:"))
if num>0:
    print("Positive number")
elif num<0:
    print("Negative number") 
else:
    print("Zero")