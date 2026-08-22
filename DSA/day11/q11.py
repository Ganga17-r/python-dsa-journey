# Find the Smallest Element
arr = [12, 34, 2, 4, 5, 6, 17]
smallest=arr[0]
for i in range(len(arr)):
    if arr[i]<smallest:
        smallest=arr[i]
print("smallest:",smallest)