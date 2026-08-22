# Day 9 - Second Largest (Improved)

arr = [8, 15, 12, 19, 5]

largest = arr[0]
second_largest = None

for i in range(1, len(arr)):

    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]

    elif arr[i] != largest:

        if second_largest is None or arr[i] > second_largest:
            second_largest = arr[i]

print("Largest:", largest)

if second_largest is None:
    print("Second Largest: Not Found")
else:
    print("Second Largest:", second_largest)