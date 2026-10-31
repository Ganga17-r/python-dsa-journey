'''Problem 2: largest_of_three(a, b, c) returns the biggest of the three numbers. Do not use max().

largest_of_three(4, 9, 2) → 9'''

#largest_of_three(10, 3, 7) → 10
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >=c:
        return b
    else:
        return c
print(largest_of_three(4, 9, 2))
print(largest_of_three(10, 3, 7))
print(largest_of_three(5, 5, 3))