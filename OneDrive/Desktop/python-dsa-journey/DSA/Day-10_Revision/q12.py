# Find the Average of all elements in the array.
arr=[1,2,3,4,5,6]
average=0
sum=0
for i in range(len(arr)):
    sum= sum + arr[i]
    average=sum/len(arr)
print(average)