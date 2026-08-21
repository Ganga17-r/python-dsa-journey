# Insert 7 at index 3.
arr = [2, 4, 6, 8, 10, 12]
arr.append(0)
for i in range(5, 2,-1):
     arr[i+1]=arr[i]
arr[3]=7
print(arr) 