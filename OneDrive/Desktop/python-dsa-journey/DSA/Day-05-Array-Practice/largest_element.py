arr=[1,2,3,4,0.5]
largest=arr[0]
for i in range(len(arr)):
    if largest<arr[i]:
        largest=arr[i]
print(largest)