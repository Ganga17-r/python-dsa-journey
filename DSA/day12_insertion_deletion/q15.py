# Delete 15 at index 2.
arr = [5, 10, 15, 20, 25, 30]
for i in range(3,6,1):
    arr[i-1]=arr[i]     
arr.pop()
print(arr)