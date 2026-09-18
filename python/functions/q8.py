# Write a function:count_positive(numbers)
numbers = [-2, 5,-7, 8, 0, 3, -1]
def count_positive(numbers):
    count=0
    for n in numbers:
        if n>0:
            count=count+1
    return count
print(count_positive(numbers))
