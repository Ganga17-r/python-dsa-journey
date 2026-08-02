# Day 9 - Move Zeros to End

arr = [1, 0, 2, 0, 3, 4]

result = []

for i in range(len(arr)):
    if arr[i] != 0:
        result.append(arr[i])

zero_count = len(arr) - len(result)

for i in range(zero_count):
    result.append(0)

print(result)