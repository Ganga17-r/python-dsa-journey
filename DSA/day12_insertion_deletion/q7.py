# Insert 10 at index 3.
arr = [3, 6, 9, 12, 15, 18, 21]
arr.append(0)
for i in range(6,2,-1):
    arr[i+1]=arr[i]
arr[3]=10
print(arr)