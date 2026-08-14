# Count ODD numbers.
arr=[1,2,3,4,4,44,5,66,777]
count=0
for i in range(len(arr)):
    if arr[i]%2!=0:
        count=count+1
print("count:",count)