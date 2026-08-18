# Insert 10 at index 0.
arr = [20, 30, 40, 50]
arr.append(0)
for i in range(3,-1,-1):
    arr[i+1]=arr[i]
arr[0]=10
print(arr)