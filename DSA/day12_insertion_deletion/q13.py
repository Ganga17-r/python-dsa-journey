# Delete 12 at index 2.
arr = [4, 8, 12, 16, 20, 24, 28, 32]
for i in range(3,8,1):
    arr[i-1]=arr[i]
arr.pop()
print(arr)