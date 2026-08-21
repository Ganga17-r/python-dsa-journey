# Delete 20 at index 3.
arr = [5, 10, 15, 20, 25, 30, 35]
for i in range(4,7,1):
    arr[i-1]=arr[i]
arr.pop()
print(arr)