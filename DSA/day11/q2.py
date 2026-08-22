# Problem-2
# Check if the Array is Sorted.

arr = [1, 2, 3, 4, 5]

sorted = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        sorted = False
        break

if sorted:
    print("Sorted")
else:
    print("Not Sorted")