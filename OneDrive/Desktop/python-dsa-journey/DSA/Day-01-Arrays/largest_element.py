# Day 1 - Arrays
# Problem: Find the largest element in an array

arr = [7, 2, 9, 1, 5]
largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest:", largest)