# Find the Second Smallest Element
arr = [12, 34, 2, 4, 5, 6, 17]
smallest=arr[0]
second_smallest=arr[0]
for i in range(len(arr)):
    if arr[i]<smallest:
        second_smallest = smallest
        smallest = arr[i]
    elif arr[i]>smallest and second_smallest>arr[i]:
        second_smallest=arr[i]
print("second_smallest:",second_smallest)