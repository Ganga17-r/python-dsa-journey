# Insert 25 at index 2 in the array [10, 20, 30, 40, 50].
arr=[10, 20, 30, 40, 50]
arr.append(0)
for i in range(4,1,-1):
    arr[i+1]=arr[i]
arr[2]=25
print(arr)
