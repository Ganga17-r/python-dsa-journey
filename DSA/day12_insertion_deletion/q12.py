# Delete 66 at index 5.
arr = [11, 22, 33, 44, 55, 66, 77]
for i in range(6,7,1):
    arr[i-1]=arr[i]
arr.pop()
print(arr)