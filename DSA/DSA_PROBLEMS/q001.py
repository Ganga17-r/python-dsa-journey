'''Problem 1: is_even(n) returns True if n is even, otherwise False.

is_even(8) → True
is_even(7) → False'''
a=int(input("Enter a number: "))
if a%2==0:
    print("True")

else:
    print("False")

def is_even(n):
    if n%2==0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(9))