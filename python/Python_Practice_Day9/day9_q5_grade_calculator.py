#Problem: Grade Calculator (Basic)

'''Take marks as input.

Rules:
Marks 90 or above → Grade A
Marks 75 to 89 → Grade B
Marks 50 to 74 → Grade C
Below 50 → Fail'''
marks=int(input("Enter your marks:"))
if marks>=90:
    print("Grade A")
elif marks>=75 and marks<=89:
    print("Grade B")
elif marks>=50 and marks<=74:
    print("Grade C")
else:
    print("Fail")