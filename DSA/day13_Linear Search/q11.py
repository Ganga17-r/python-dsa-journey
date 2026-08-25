#question -11Q
arr = [4, 15, 9, 27, 6]
target = 100
index=-1
for i in range(len(arr)):
    if arr[i]==target:
        index=i
print(index)