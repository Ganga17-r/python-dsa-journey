# find the index of 28.
arr=[11,6,28,17,35]
target = 28
index=-1
for i in range(len(arr)):
    if arr[i]==28:
        index=i
        break
print(index)