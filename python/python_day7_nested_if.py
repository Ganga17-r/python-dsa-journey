# Day 7 - Nested if Statement

age = int(input("Enter your age: "))

if age >= 18:
    if age >= 21:
        print("You are eligible to vote and drive.")
    else:
        print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")