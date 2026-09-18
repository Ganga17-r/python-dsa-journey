# Write a function:average(numbers)
# It should return the average of all numbers in the list.
numbers = [10, 20, 30, 40, 50]
def average(numbers):
    total=0
    for n in numbers:
        total=total+n
    average = total / len(numbers)
    return average
print(average(numbers))