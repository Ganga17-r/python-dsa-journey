# Insert 50 at index 5.
arr = [11, 22, 33, 44, 55, 66]
arr.append(0)
for i in range(5,4,-1):
    arr[i+1]=arr[i]
arr[5]=50
print(arr)