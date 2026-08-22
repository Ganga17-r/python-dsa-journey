# Find the Second Largest Element
arr = [12, 34, 2, 4, 5, 6, 17]
largest=arr[0]
second_largest=arr[0]
for i in range(len(arr)):
    if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
    elif arr[i] < largest and second_largest<arr[i]:
         second_largest = arr[i]
print("second_largest:",second_largest)
    