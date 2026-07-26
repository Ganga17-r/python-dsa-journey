arr=[1,2,3,-3,-4,-6,6]
sum=0
for i in range(len(arr)):
    if arr[i]<0:
        sum=sum+arr[i]
print(sum)