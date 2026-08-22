#  Count how many times 9 appears in the array.
arr=[1,3,9,8,56,9,6,4,89]
count=0
for i in range(len(arr)):
    if arr[i]==9:
        count=count+1
print("count:",count)