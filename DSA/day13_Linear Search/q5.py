#problem-5
#arr = [6, 14, 22, 31, 45]
# target = 50
arr = [6, 14, 22, 31, 45]
index="not found"
for i in range(len(arr)):
    if arr[i]==50:
        index=i
        break
print(index)
