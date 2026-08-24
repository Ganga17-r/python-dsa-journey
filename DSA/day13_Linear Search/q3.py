#problem -3
# # arr = [5, 12, 8, 20, 12, 30]
# target = 12
arr = [5, 12, 8, 20, 12, 30]
index=-1
for i in range(len(arr)):
    if arr[i]==12:
        index=i
        break #break: stops at first match, first occurrence gets stored
print(index)