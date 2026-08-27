#q9-Find the sum of numbers that are NOT divisible by 3.
num = [12, 7, 25, 18, 30, 9, 41, 20]
total=0
for i in range(len(num)):
    if num[i]%3==0:
        continue
    total=total+num[i]
print(total)