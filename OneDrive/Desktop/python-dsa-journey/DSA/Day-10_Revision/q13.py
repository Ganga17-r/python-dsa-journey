# Find the Largest Element in the Array.
arr=[12,34,2,4,5,6,17]
largest=0
for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]
print(largest)