# Q15 — Find the sum of numbers between 10 and 40
num = [5, 12, 25, 45, 18, 30, 9, 50, 35]
total=0
for i in range(len(num)):
    if num[i]>=10 and num[i]<=40:
        total=total+num[i]
print(total)
