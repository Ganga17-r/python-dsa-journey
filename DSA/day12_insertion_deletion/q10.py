# Beginning of the array,Delete 10, which is at index 0.
arr = [10, 20, 30, 40, 50]
for i in range(1,5,1):
    arr[i-1]=arr[i]
arr.pop()
print(arr)