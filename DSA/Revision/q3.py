arr = [18, 7, 25, 7, 40, 12]
target = 7
index = -1
for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break
print(index)