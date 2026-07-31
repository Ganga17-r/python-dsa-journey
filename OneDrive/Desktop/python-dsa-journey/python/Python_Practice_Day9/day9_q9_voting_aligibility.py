#Problem-9
'''Problem Statement

Write a Python program that asks the user to enter:
Age
Citizenship (yes or no)

The program should check whether the person is eligible to vote.

Rules:
If the person's age is 18 or above
AND
The person is a citizen (yes)'''
age=int(input("Enter your age:"))
citizenship=input("Are you an Indian citizen? (yes/no):")
if age>=18 and citizenship=="yes":
    print("eligible to vote")
else:
    print("not eligible")
