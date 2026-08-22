#problem-6
'''find the Largest of Three Numbers
Take three numbers from the user.
Print:Largest number is: __'''
num1=int(input("enter your number:"))
num2=int(input("enter your number:"))
num3=int(input("enter your number:"))
if num1>=num2 and num1>=num3:
    print("Largest number:",num1)
elif num2>=num1 and num2>=num3:
    print("largest number:", num2)
elif num3>=num1 and num3>=num2:
    print("Largest number:",num3)