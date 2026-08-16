# Find the index of the smallest element

arr = [12, 34, 2, 4, 5, 6, 17]

smallest = arr[0]
smallest_index = 0

for i in range(len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]
        smallest_index = i

print("smallest_element_index:", smallest_index)