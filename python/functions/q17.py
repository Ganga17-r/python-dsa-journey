# Count even numbers using '*args'---*args → collects values
def count_even(*args):
    count = 0
    for n in args:
        if n % 2 == 0:
          count=count+1
    return count
print(count_even(10, 7, 4, 13, 20, 9, 6))