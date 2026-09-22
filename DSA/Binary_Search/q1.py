#Binary Search — Q1
#Problem-Find the index of 60 using Binary Search.

arr = [10, 20, 30, 40, 50, 60, 70]
target = 60
low = 0
high = len(arr) - 1
mid = (low + high) // 2
if arr[mid] < target:
    low = mid + 1
    while low <= high:
