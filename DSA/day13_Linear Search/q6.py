#problem-6
#arr = [4, 9, 15, 9, 22]
# target = 9
arr=[4,9,15,9,22]
index=-1
for i in range(len(arr)):
    if arr[i]==9:
        index=i
        break
print(index)