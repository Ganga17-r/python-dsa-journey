arr = [5, 12, 8, 20, 12, 30]
target = 12
index = -1
for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break
print(index)