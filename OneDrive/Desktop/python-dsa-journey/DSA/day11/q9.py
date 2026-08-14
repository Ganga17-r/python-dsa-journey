#find the average
arr = [1, 2, 3, 3, 2, 24, 4, 4]

sum = 0

for i in range(len(arr)):
    sum = sum + arr[i]

average = sum / len(arr)

print("average:", average)