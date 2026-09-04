'''Q1-count how many numbers are even

Given:

numbers = [10, 15, 20, 25, 30]

Use a for loop to count how many numbers are even.'''
numbers = [10, 15, 20, 25, 30]
count=0
for i in range(len(numbers)):
    if numbers[i]%2==0:
        count=count+1
print(count)