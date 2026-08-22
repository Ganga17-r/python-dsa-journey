arr=[1,2,3,4,5,6]
sum=0
for i in range(len(arr)):
    if arr[i]%2!=0:
        sum=sum+arr[i]
print(sum)