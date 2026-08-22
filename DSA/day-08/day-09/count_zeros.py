# Day 9 - Count Zeros in an Array

arr = [1, 0, 2, 0, 3, 0]

count = 0

for i in range(len(arr)):
    if arr[i] == 0:
        count = count + 1

print("Number of zeros:", count)