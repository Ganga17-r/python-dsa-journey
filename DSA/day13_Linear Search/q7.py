#problem-7
#arr = [11, 6, 28, 17, 35]
# target = 17
arr=[11,6,28,17,35]
target = 17
index=-1
for i in range(len(arr)):
    if arr[i]==17:
        index=target
        break
print(index)