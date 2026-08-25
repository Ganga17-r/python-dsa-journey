# Linear Search — Q9
arr = [50, 12, 8, 31, 19, 31]
target = 31
index=-1
for i in range(len(arr)):
    if arr[i]==target:
        index=i
        break
print(index)