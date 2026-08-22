arr = [8, 15, 2, 19, 5]

smallest = arr[0]
second_smallest = arr[0]

for i in range(len(arr)):
    if arr[i] < smallest:
        second_smallest = smallest
        smallest = arr[i]

print("Smallest:", smallest)
print("Second Smallest:", second_smallest)