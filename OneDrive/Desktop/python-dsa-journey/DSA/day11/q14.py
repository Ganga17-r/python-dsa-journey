# Find the largest element's index

arr = [12, 34, 2, 4, 5, 6, 17]

largest = arr[0]
largest_index = 0

for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]
        largest_index = i

print("largest_element_index:", largest_index)