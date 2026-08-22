#Problem 7 – Even or Odd + Positive or Negative

'''Take one number from the user.

Print both:
ex-
Positive Number
Even Number
Negative Number
Odd Number'''
num=int(input("Enter your number:"))
#first decision
if num>0:
    print("Positive number")
elif num<0:
    print("negative number")
else:
    print("zero")
#second decision
if num%2==0:
    print("Even number")
else:
    print("Odd number")