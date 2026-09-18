# find the largest number from any number of arguments.

def largest(*args):
    
    largest = args[0]
    for n in args:
        if n > largest:
         largest = n
    return largest
print(largest(10, 25, 7, 40, 18))