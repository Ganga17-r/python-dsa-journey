# Insert 35 at index 4.
arr = [10, 20, 30, 40, 50]
arr.append(0)
for i in range(4,3,-1):
    arr[i+1]=arr[i]
arr[4]=35
print(arr)