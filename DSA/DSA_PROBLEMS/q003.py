'''Problem 3

Problem 3: grade(marks) returns "A" if marks are 75 or more,
 "B" if marks are 50 or more, otherwise "C".

grade(80) → "A"
grade(60) → "B"
grade(30) → "C"'''
def grade(n):
    if n>=75:
        return "A"
    elif n>=50:
        return "B"
    else:
        return "C"
print(grade(80))
print(grade(60))
print(grade(30))
print(grade(75))
print(grade(50))