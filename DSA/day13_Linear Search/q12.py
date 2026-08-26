# Q12 — Count Occurrences
arr = [5, 2, 5, 8, 5, 10]
target = 5
count=0
index=-1
for i in range(len(arr)):
    if arr[i]==5:
        index=i
        count=count+1
print(count)