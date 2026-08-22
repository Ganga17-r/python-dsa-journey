#problem-8
'''
Take the year from the user.
Check:
-year % 4 == 0
-If True → Print "Leap Year"
-Else → Print "Not a Leap Year"'''
year=int(input("enter your year:"))
if year%4==0:
    print("Leap year")
else:
    print("not a Leap year")