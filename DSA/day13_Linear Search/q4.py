#problem-4
# arr = [18, 7, 25, 7, 40, 12]
# target = 7
arr = [18, 7, 25, 7, 40, 12]
index=-1
for i in range(len(arr)):
    if arr[i]==7:
        index=i
        break
print(index)