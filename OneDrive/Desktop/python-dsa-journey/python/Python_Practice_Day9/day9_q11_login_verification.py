#Problem Statement

'''Write a Python program that asks the user to enter:
Username
Password
Assume the correct credentials are:
Username: admin
Password: 1234
RulesIf both the username and password are correct, print:
Login Successful
Otherwise print:
Invalid Username or Password'''
Username=input("Enter Username:")
Password=input("Enter Password:")
if Username=="admin" and Password=="1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")