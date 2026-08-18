# Insert 15 at index 1 arr = [10, 20, 30, 40, 50]
arr = [10, 20, 30, 40, 50]
arr.append(0)

for i in range(4,0,-1):
    arr[i+1]=arr[i]
arr[1]=15
print(arr)