# Count how many EVEN numbers are in the array.
arr = [2, 3, 4, 5, 6]
count=0
for i in range(len(arr)):
    if arr[i]%2==0:
        count=count+1
print("count:",count)