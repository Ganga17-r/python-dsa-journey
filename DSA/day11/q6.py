# Count EVEN numbers
arr=[1,2,3,4,3,45,55,66,7,89,0]
count=0
for i in range(len(arr)):
    if arr[i]%2==0:
        count=count+1
print("count:",count)