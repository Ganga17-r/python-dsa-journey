arr = [20, 5, 15, 30]

smallest = arr[0]
largest = arr[0]

for i in range(len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]

    if arr[i] > largest:
        largest = arr[i]

difference = largest - smallest

print(difference)