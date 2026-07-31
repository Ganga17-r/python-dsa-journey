#problem-13
'''Problem Statement
A company wants to give a festival bonus to its employees.
Write a Python program that asks the user to enter:
Years of Experience
Salary
Rules
The employee gets a bonus only if:
Experience is 5 years or more
AND
Salary is less than 50,000
If eligible, print:
Bonus Approved 🎉
Otherwise print:
Bonus Not Approved'''
Experience=int(input("Enter your years of experience:"))
Salary=int(input("enter your salary:"))
if Experience>=5 and Salary<50000:
    print("Bonus Approved 🎉")
else:
    print("Bonus not found")
