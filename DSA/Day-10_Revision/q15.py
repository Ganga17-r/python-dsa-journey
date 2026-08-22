# Problem-15
# Find the Second Largest Element in the Array.

arr = [23, 44, 2, 3, 5, 6, 11]

largest = arr[0]
second_largest = arr[0]

for i in range(1, len(arr)):   # Start from index 1
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]

    elif arr[i] > second_largest:
        second_largest = arr[i]

print("Largest:", largest)
print("Second Largest:", second_largest)