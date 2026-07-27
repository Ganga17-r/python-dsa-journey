arr = [8, 15, 2, 19, 5]

largest = arr[0]
second_largest = arr[0]

for i in range(len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]

print("Largest:", largest)
print("Second Largest:", second_largest)