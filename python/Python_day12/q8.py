#q8-Find the sum of numbers that are NOT divisible by 5.
num = [10, 13, 20, 27, 31, 35, 42, 45, 50]
total=0
for i in range(len(num)):
    if num[i]%5==0:
        continue
    total=total+num[i]
print(total)
