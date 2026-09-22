arr=[10,9,20,30,40,50]
target=20
index = -1
for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break
print(index)