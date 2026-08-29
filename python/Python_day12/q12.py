#12q-Find the sum of only the positive numbers.
num = [12, 5, 0, 18, -3, 25, 7, -10, 30]
total=0
for i in range(len(num)):
    if num[i]<0:
        continue
    total=total+num[i]
print(total)