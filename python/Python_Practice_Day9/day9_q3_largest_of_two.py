#Practice-3
#Largest of Two Numbers
#take two numbers from the user.

#Print:The largest number, or "Both numbers are equal" if they are the same.
num1=int(input("Enter your number:"))
num2=int(input("Enter your number:"))
if num1>num2:
    print("Largest number is :",num1)
elif num2>num1:
    print("Largest number is :",num2)
else:
    print("Both numbers are equal")
    