#problem-12
'''Problem Statement

Write a Python program that asks the user to enter:

Account Balance
Withdrawal Amount

The program should check whether the withdrawal is possible.

Rules
If the withdrawal amount is less than or equal to the account balance, print:
Transaction Successful
Remaining Balance: __
Otherwise print:
Insufficient Balance'''

Account_Balance=int(input("enter your account balance:"))
Withdrawal_amount=int(input("enter withdrawal amount:"))
if Account_Balance>=Withdrawal_amount:
    print("Transaction Successful")
    print("Remaining_Balance:", Account_Balance-Withdrawal_amount)
else:
    print("Insufficient Balance")