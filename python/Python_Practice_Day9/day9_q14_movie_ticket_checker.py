#problem-14
'''Problem Statement
A movie theater has a rule for allowing entry.
Write a Python program that asks the user to enter:
Age
Has Ticket? (yes or no)
Rules
A person can enter the theater only if:
Age is 18 or above
AND
The person has a ticket (yes)
If eligible, print:
Entry Allowed 🎬
Otherwise print:
Entry Denied ❌'''
Age=int(input("enter your age:"))
ticket=input("have tickets(yes/no):")
if Age>=18 and ticket=="yes":
    print("Entry allowed")
else:
    print("Entry Denied")
