# question-10Q
arr = [7, 18, 25, 18, 40, 52]
target = 18
index=-1
for i in range(len(arr)):
    if arr[i]==target:
     index=i
     break
print(index)