# Problem-14

# Find the Smallest Element in the Array./
arr = [12, 34, 2, 4, 5, 6, 17]
smallest=arr[0]
for i in range(len(arr)):
    if arr[i]<smallest:
        smallest=arr[i]
print("smallest:", smallest)
