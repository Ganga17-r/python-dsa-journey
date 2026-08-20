# Delete the element 30 from index 2.
arr = [10, 20, 30, 40, 50]
for i in range(3,5,1):
    arr[i-1]=arr[i]
arr.pop()
print(arr)